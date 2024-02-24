#ifndef HT_H
#define HT_H

#include <stdio.h>

typedef int bool;

bool is_happy_ticket(int num);

#endif

int is_happy_ticket(int num) {
  int sum1 = 0, sum2 = 0;
  while (num > 0) {
    sum1 += num % 10;
    num /= 10;
    sum2 += num % 10;
    num /= 10;
  }
  return sum1 == sum2;
}