#include <stdio.h>

int pow (int base, int exponent) {
	int result = 1;
	while (exponent-- > 0)
		result *= base;
	return result;
}

double pi (int n) {
	int i;
	double pi = 0;

	for (i = 0; i < n; i++)
		pi +=  pow(-1, i) * 4.0 / (2 * i + 1);
	return pi;
}

int main() {
	int epsilon;

	printf("Este programa calcula o valor aproximado de π fazendo uso da fórmula de Leibniz. O grau de precisão do resultado é dado pelo valor de epsilon, um número inteiro e não negativo.\nDigite um valor para epsilon: ");
	if (scanf(" %d", &epsilon) == EOF || epsilon < 0) {
		printf("Valor inválido");
		return 1;
	}
	printf("O valor aproximado de π para epsilon = %d é: %lf\n", epsilon, pi(epsilon));
	return 0;
}
