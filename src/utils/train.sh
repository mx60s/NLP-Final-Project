# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

SAVE_DIR=../checkpoints/RE-WhiteText-BioGPT/positive_tagged
mkdir -p ${SAVE_DIR}

fairseq-train \
    ../data/tagged_data/pos_only --save-dir ${SAVE_DIR} \
    --user-dir /content/gdrive/MyDrive/nlp-final/NLP-Final-Project/src/src \
    --finetune-from-model ../checkpoints/Pre-trained-BioGPT/checkpoint.pt \
    --task language_modeling_prompt \
    --arch transformer_lm_prompt_biogpt \
    --share-decoder-input-output-embed --decoder-learned-pos \
    --optimizer adam --adam-betas '(0.9, 0.98)' \
    --weight-decay 0.01 --clip-norm 0.0 \
    --lr 1e-5 --lr-scheduler inverse_sqrt --warmup-updates 100 --warmup-init-lr 1e-07 \
    --tokens-per-sample 1024 --max-source-positions 640 --max-target-positions 1024 \
    --max-tokens 1024 --update-freq 32 \
    --skip-invalid-size-inputs-valid-test \
    --max-epoch 50 --keep-last-epochs 2 \
    --learned-prompt 9