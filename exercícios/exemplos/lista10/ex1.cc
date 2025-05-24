// #include <iostream> 
// #include <cuda_runtime.h> 
 
// #define N 1024  // Tamanho dos vetores 
// #define THREADS_PER_BLOCK 256 
 
// // Kernel CUDA para somar dois vetores 
// __global__ void somaVetores(float *a, float *b, float *c, int n) { 
//     int i = blockIdx.x * blockDim.x + threadIdx.x; 
//     if (i < n) 
//         c[i] = a[i] + b[i]; 
// } 
 
// int main() { 
//     // Vetores na CPU (host) 
//     float *h_a, *h_b, *h_c; 
 
//     // Vetores na GPU (device) 
//     float *d_a, *d_b, *d_c; 
 
//     size_t size = N * sizeof(float); 
 
//     // Aloca memória na CPU 
//     h_a = (float*)malloc(size); 
//     h_b = (float*)malloc(size); 
//     h_c = (float*)malloc(size); 
 
// 2 
 
 
//     // Inicializa os vetores a e b 
//     for (int i = 0; i < N; i++) { 
//         h_a[i] = i * 1.0f; 
//         h_b[i] = i * 2.0f; 
//     } 
 
//     // Aloca memória na GPU 
//     cudaMalloc((void**)&d_a, size); 
//     cudaMalloc((void**)&d_b, size); 
//     cudaMalloc((void**)&d_c, size); 
 
//     // Copia dados da CPU para GPU 
//     cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice); 
//     cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice); 
 
//     // Executa o kernel na GPU 
//     int blocks = (N + THREADS_PER_BLOCK - 1) / THREADS_PER_BLOCK; 
//     somaVetores<<<blocks, THREADS_PER_BLOCK>>>(d_a, d_b, d_c, N); 
 
//     // Espera a GPU terminar 
//     cudaDeviceSynchronize(); 
 
//     // Copia resultado de volta para CPU 
//     cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost); 
 
//     // Exibe os primeiros 10 resultados 
//     std::cout << "Soma dos vetores (primeiros 10 valores):\n"; 
//     for (int i = 0; i < 10; i++) { 
//         std::cout << h_a[i] << " + " << h_b[i] << " = " << h_c[i] << std::endl; 
//     } 
 
// 3 
 
 
//     // Libera memória 
//     cudaFree(d_a); 
//     cudaFree(d_b); 
//     cudaFree(d_c); 
//     free(h_a); 
//     free(h_b); 
//     free(h_c); 
 
//     return 0; 
// }