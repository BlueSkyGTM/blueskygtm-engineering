# Exercises — Vision-Language Models â€” The ViT-MLP-LLM Pattern

## Exercises

1. **Compute patch token counts for a range of image resolutions and patch sizes.** Write a Python script that accepts an image resolution (height × width) and a patch size, then prints the number of visual tokens the ViT will produce. Run your script for these five configurations and print the results in a formatted table: (224×224, 14), (224×224, 16), (448×448, 14), (384×384, 16), (1024×1024, 14). Include a column showing the ratio of tokens to the 224×224/14 baseline.

2. **Implement a forward pass through patch embedding and MLP projection on a synthetic image tensor.** Using only `torch` and `torch.nn`, create a random tensor of shape `(1, 3, 336, 336)` representing a single RGB image. Build a patch embedding layer (`Conv2d` or `Linear` over flattened patches) with patch size 14 and `d_vit = 1024`, then a two-layer MLP projector with GELU activation mapping from `d_vit` to `d_llm = 4096`. Run the forward pass and print the tensor shape after each stage: raw input → flattened patches → patch embeddings → projected visual tokens. Verify that the final shape matches your token-count calculation from Exercise 1.

3. **Build a configurable dimension-trace function and compare two model configurations.** Implement `trace_vlm_dimensions(image_h, image_w, patch_size,
