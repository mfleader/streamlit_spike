import os
import enum

import streamlit as st
import elasticsearch as es
import pandas as pd
import pandasticsearch as pdsh


class PipelineStatus(enum.Enum):
    red = 'failure'
    yellow = 'unstable'
    green = 'success'


def main():
    url = os.getenv('ELASTICSEARCH_URL')
    index = 'mb'
    db = es.Elasticsearch(
        url
    )    
    st.title('Pipelines')
    table = db.search(index='mb')
    df1 = pdsh.Select.from_dict(table).to_pandas()
    st.write(df1)
    pipedf = pd.DataFrame.from_records(
        data=(
            ('aws', 'failure'),
            ('aws future', 'succes'),
            ('aws next', 'unstable'),
            ('aws ovn next', 'success'),
            ('azure', 'failure'),
            ('gcp', 'failure')
        ),
        columns=['pipeline', 'status']
    )
    # would have to inject css styling here
    if st.button('show pipeline info'):
        st.write(pipedf)
    else:
        st.write('nothing to see here')



if __name__ == '__main__':
    main()
