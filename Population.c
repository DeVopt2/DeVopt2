#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size

    // TODO: Prompt for end size

    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years

    float b = (.25);
    float m = (.33);

    int stn, enn;

    // printf statement
    printf("This Program Calculates Years To Reach An Entered Population Of Lamma based on yearly relative frequency distributions of: birth %f mortality %f\n",b, m);

    do
    {
        stn = get_int("LAMMA STARTING POPULATION NUMBER:Enter A Whole Number 9 Or Higher:   ");
    }

    while (stn < 9);

    do
    {
        enn = get_int("LAMMA ENDING POPULATION NUNBER:Enter A Whole Number Equal To Or Higher Than Your Starting Number:   ");
    }
    while (enn < stn);

    /*calculating years to reach population number based on yearly birth and mortality percentages*/

    float y1 = (float) stn / 3 - (float) stn / 4;
    float y2 = (float) (enn - stn)/y1;

    // Years to reach ending number
    printf("Years: %f\n", y2);

    return 0;
}
