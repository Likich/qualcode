# generation_config = model.generation_config
# generation_config.max_new_tokens = 10
# generation_config.temperature = 0.7
# generation_config.top_p = 0.7
# generation_config.num_return_sequences = 1
# generation_config.pad_token_id = tokenizer.eos_token_id
# generation_config.eos_token_id = tokenizer.eos_token_id
def combine_data(file1, file2):
    import pandas as pd

    df_raw = pd.read_csv(file1)
    clusters_documents = pd.read_csv(file2)

    combined_df = pd.merge(df_raw, clusters_documents, left_index=True, right_on='Doc_ID')

    # Check the combined dataframe
    print(combined_df.head(20))


    df = combined_df[['paragraphs', 'Topic', 'Doc']]
    df.to_csv('doc_topics.csv', index=False)


