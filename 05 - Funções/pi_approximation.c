#include <stdio.h>

double pi (int n) {
	int i;
	double pi = 0, step;

	for (i = 0; i < n; i++) {
		step = 4.0 / (2 * i + 1);
		pi +=  (i % 2 == 0) ? step : -step;
	}
	return pi;
}

int main() {
	int epsilon;

	printf("Este programa calcula o valor aproximado de π fazendo uso da fórmula de Leibniz. O grau de precisão do resultado é dado pelo valor de epsilon, um número inteiro e não negativo.\nDigite um valor para epsilon e pressione ENTER: ");

	if (scanf(" %d", &epsilon) == EOF) {
		printf("Erro: não é um valor inteiro.\n");
		return 1;
	}
	if (epsilon < 0) {
		printf("Erro: valor negativo.\n");
		return 1;
	}
	printf("O valor aproximado de π para epsilon = %d é: %.16lf\n", epsilon, pi(epsilon));
	return 0;
}
