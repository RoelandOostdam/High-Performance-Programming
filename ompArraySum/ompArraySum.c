/* arraySum.c uses an array to sum the values in an input file,
 *  whose name is specified on the command-line.
 * Huib Aldewereld, HU, HPP, 2020
 */

#include <stdio.h>      /* I/O stuff */
#include <stdlib.h>     /* calloc, etc. */
#include <omp.h>

void readArray(char * fileName, double ** a, int * n);
double sumArray(double * a, int numValues, int n);
double measureTime(double * a, int numValues, int n);

int main(int argc, char * argv[])
{
	int  howMany;
	double sum;
	double * a;
	double time_taken;

	if (argc != 2) {
		fprintf(stderr, "\n*** Usage: arraySum <inputFile>\n\n");
		exit(1);
	}
	
	
	readArray(argv[1], &a, &howMany);
	// sum = sumArray(a, howMany, 4);
	double thread_options[4] = {1,2,4,8};
	int test_amount = 1000;
	double times[4][test_amount];

	for (int n1 = 0; n1 < 4; n1++) {
		for(int n2=0;n2<test_amount;n2++){
			time_taken = measureTime(a, howMany, thread_options[n1]);
			printf("Threads: %g || Iteration: %i || Time: %f \n", thread_options[n1], n2, time_taken);
			times[n1][n2] = time_taken;
		}
	}
	for (int n1 = 0; n1 < 4; n1++) {
		double total = 0;
		for(int x=0;x<test_amount;x++){
			total+=times[n1][x];
		}
		printf("The average time for n=%g is %f\n",thread_options[n1],total/test_amount);
	}
	// printf("The sum of the values in the input file '%s' is %g\n",
	// 				 argv[1], sum);
	free(a);

	return 0;
}

/* readArray fills an array with values from a file.
 * Receive: fileName, a char*,
 *          a, the address of a pointer to an array,
 *          n, the address of an int.
 * PRE: fileName contains N, followed by N double values.
 * POST: a points to a dynamically allocated array
 *        containing the N values from fileName
 *        and n == N.
 */

void readArray(char * fileName, double ** a, int * n) {
	int count, howMany;
	double * tempA;
	FILE * fin;

	fin = fopen(fileName, "r");
	if (fin == NULL) {
		fprintf(stderr, "\n*** Unable to open input file '%s'\n\n",
										 fileName);
		exit(1);
	}

	fscanf(fin, "%d", &howMany);
	tempA = calloc(howMany, sizeof(double));
	if (tempA == NULL) {
		fprintf(stderr, "\n*** Unable to allocate %d-length array",
										 howMany);
		exit(1);
	}

	for (count = 0; count < howMany; count++)
	 fscanf(fin, "%lf", &tempA[count]);

	fclose(fin);

	*n = howMany;
	*a = tempA;
}

/* sumArray sums the values in an array of doubles.
 * Receive: a, a pointer to the head of an array;
 *          numValues, the number of values in the array.
 * Return: the sum of the values in the array.
 */

double measureTime(double *a, int numValues, int numThreads){
	double start = omp_get_wtime();
	sumArray(a, numValues, numThreads);
	double end = omp_get_wtime();
	return end - start;
}

double sumArray(double *a, int numValues, int numThreads){
	int i;
	double result = 0.0;

#pragma omp parallel for reduction(+ : result) num_threads(numThreads)
	for (i = 0; i < numValues; i++)
	{
		result += a[i];
	}

	return result;
}

