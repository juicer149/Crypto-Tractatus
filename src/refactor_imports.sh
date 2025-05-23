#!/bin/bash

declare -A changes=(
  ["lib.alphabet.base_alphabet"]="structures.alphabet"
  ["lib.alphabet.rotation_table"]="structures.rotation_table"
  ["lib.core.concepts"]="core.concept"
  ["lib.core.error"]="core.error"
  ["lib.core.base_engine"]="core.base_engine"
  ["lib.sequences.sequence"]="structures.sequence"
  ["lib.sequences.transform"]="transforms.sequence_ops"
  ["lib.utils.mapping"]="meta.registry"
  ["lib.concepts.vigenere"]="ciphers.vigenere_cipher"
  ["lib.concepts.multi_vigenere"]="ciphers.multi_vigenere_cipher"
  ["lib.concepts.rot"]="ciphers.rot_cipher"
  ["lib.sequences.math"]="math.sequence_math"
  ["lib.registry"]="meta.registry"
  ["lib.multi.strategies"]="strategies.strategies"
)

for old in "${!changes[@]}"; do
  new=${changes[$old]}
  echo "Replacing $old → $new"
  find . -type f -name "*.py" -exec sed -i "s|from $old|from $new|g" {} +
done

