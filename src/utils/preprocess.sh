# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

DATA_DIR=../data/tagged_data/pos_only
prefix=relis
OUTPUT_DIR=${DATA_DIR}/${prefix}-bin

SPLIT=(train valid test)

for ff in ${SPLIT[@]}; do
    if [ -f "${DATA_DIR}/${prefix}_$ff.y" ]; then
        echo "Preprocessing ${ff}"

        perl ${MOSES}/scripts/tokenizer/tokenizer.perl -l en -a -threads 8 < ${DATA_DIR}/${prefix}_$ff.x > ${DATA_DIR}/${prefix}_$ff.tok.x
        perl ${MOSES}/scripts/tokenizer/tokenizer.perl -l en -a -threads 8 < ${DATA_DIR}/${prefix}_$ff.y > ${DATA_DIR}/${prefix}_$ff.tok.y

        ${FASTBPE}/fast applybpe ${DATA_DIR}/${prefix}_$ff.tok.bpe.x ${DATA_DIR}/${prefix}_$ff.tok.x ${DATA_DIR}/bpecodes
        ${FASTBPE}/fast applybpe ${DATA_DIR}/${prefix}_$ff.tok.bpe.y ${DATA_DIR}/${prefix}_$ff.tok.y ${DATA_DIR}/bpecodes

        rm ${DATA_DIR}/${prefix}_$ff.tok.x ${DATA_DIR}/${prefix}_$ff.tok.y
    fi
done

# do binarize
fairseq-preprocess \
    -s x -t y --workers 8 \
    --joined-dictionary \
    --trainpref ${DATA_DIR}/${prefix}_train.tok.bpe \
    --validpref ${DATA_DIR}/${prefix}_valid.tok.bpe \
    --testpref ${DATA_DIR}/${prefix}_test.tok.bpe \
    --destdir ${OUTPUT_DIR} \
    --srcdict ${DATA_DIR}/comb_dict.txt
