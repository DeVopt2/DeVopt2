#include <cs50.h>
#include <stdio.h>
#include <math.h>


int main(void)
{
    // TODO: Prompt for start size

    // TODO: Prompt for end size

    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years

    int b = 3,  m = 4, stn, enn, rounded_years ;   
    float y1;

    // printf statement
    printf("This Program Calculates Years To Reach An Entered Population Of Lamma Based On A Yearly  Relative Frequency Distribution Of Birth Rate: %d And Mortality Rate: %d\n",b, m);

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

    /*calculating years to reach population number based on a constant yearly birth and mortality percentage*/

 float years = 0;
while (stn <  enn) ;
{
y1 =  stn/3 - stn/4:
stn = stn + y1;
// Years will update until stn = enn
years ++;

rounded_years = (int) round(years) ;
printf("Years: %d\n", rounded_years);

    
} 
    return 0;
}





