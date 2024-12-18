import numpy as np
import scipy
from sklearn.cluster import KMeans
import matrix_util as mut


def partition_graph(graph_process_request):
    adjacency_list = graph_process_request['adjacency_list']
    partition_num = graph_process_request['partition_num']

    # Construct laplacian
    a_matrix = mut.adjacency_list_to_matrix(adjacency_list)
    affinity_matrix = mut.build_affinity_matrix(a_matrix)
    degree_matrix = mut.build_degree_matrix(affinity_matrix)
    d_i = scipy.linalg.fractional_matrix_power(degree_matrix, -0.5)
    laplacian = np.matmul(d_i, np.matmul(affinity_matrix, d_i))

    eigen_data = np.linalg.eigh(laplacian)
    ortho_eigen_matrix = mut.build_orthogonal_eigen_matrix(eigen_data)
    row_num, col_num = ortho_eigen_matrix.shape

    sampled_eigen_matrix = mut.sample_range_of_columns(ortho_eigen_matrix, col_num - partition_num, col_num)
    normalized_eigen_matrix = mut.normalized_matrix_rows(sampled_eigen_matrix)

    kmeans = KMeans(n_clusters=partition_num).fit(normalized_eigen_matrix)

    group_mapping = {}
    for i, key in enumerate(adjacency_list):
        group_mapping[key] = str(kmeans.labels_[i])
    

    return group_mapping
