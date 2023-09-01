include <cs50.h>
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
    printf("This Program Calculates Years To Reach A Given Population Of Lammas based on yearly relative frequency distributions "
           "of: birth %f mortality %f\n",
           b, m);

    do
    {
        stn = get_int("LAMMA STARTING POPULATION SIZE:Enter A Whole Number 9 Or Higher:   ");
    }

    while (stn < 9);

    do
    {
        enn = get_int("LAMMA ENDING POPULATION SIZE:Enter A Whole Number Equal To Or Higher Than Your Starting Number:   ");
    }
    while (enn < stn);

    /*calculating years to reach end
     population number based on yearly birth and mortality percentages*/

    float y1 = stn + (float) stn / 3 - (float) stn / 4;
    float y2 = (float) y1 * (enn - stn);

    // years for Lamma to reach a given number of live births
    printf("Years For Lamma To Reach A Give Number Of Live Births: %f\n", y1 + y2);

    return 0;
}
