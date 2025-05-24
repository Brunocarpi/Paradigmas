// #include <iostream> 
// #include <cuda_runtime.h> 
 
// __global__ void multiplicaEscalar(int *A, int *B, int k, int N) { 
//     int i = threadIdx.x + blockIdx.x * blockDim.x; 
//     if (i < N) { 
//         B[i] = A[i] * k; 
//     } 
// } 
 
// 4 
 
 
// int main() { 
//     const int N = 256; 
//     int *h_A = new int[N]; 
//     int *h_B = new int[N]; 
//     int *d_A, *d_B; 
//     int k = 5; 
 
//     // Inicializa o vetor A 
//     for (int i = 0; i < N; i++) { 
//         h_A[i] = i; 
//     } 
 
//     cudaMalloc(&d_A, N * sizeof(int)); 
//     cudaMalloc(&d_B, N * sizeof(int)); 
 
//     cudaMemcpy(d_A, h_A, N * sizeof(int), cudaMemcpyHostToDevice); 
 
//     // Configura 1 bloco de 256 threads 
//     multiplicaEscalar<<<1, 256>>>(d_A, d_B, k, N); 
 
//     cudaMemcpy(h_B, d_B, N * sizeof(int), cudaMemcpyDeviceToHost); 
 
//     // Imprime os primeiros 10 resultados 
//     for (int i = 0; i < 10; i++) { 
//         std::cout << "B[" << i << "] = " << h_B[i] << std::endl; 
//     } 
 
//     cudaFree(d_A); 
//     cudaFree(d_B); 
//     delete[] h_A; 
 
// 5 
 
//     delete[] h_B; 
 
//     return 0; 
// }