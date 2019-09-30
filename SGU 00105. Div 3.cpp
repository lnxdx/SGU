#include <cstdio>
#include <cstring>

int main() {
	long long n;
	scanf("%lld", &n);

	if (n % 3 != 2)
		printf("%lld\n", n / 3 * 2);
	else
		printf("%lld\n", n / 3 * 2 + 1);

	return 0;
}
