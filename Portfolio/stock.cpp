#ifndef STOCK_H
#define STOCK_H
#include<string.h>
using namespace std;

class stock{

public:
stock()
{


}
stock(string company_name, double cp, int in)
{
set_cp(cp);
set_name(company_name);
set_in(in);
}
struct option{
int strike;
double price; 
double change;
double percent_change;
double ask;
double bid;
int volume;
int open_int;
};
double price_history[100];
double get_cp(){return current_price;}
void set_cp(double price){current_price = price;}
int get_in(){return industry;}
void set_in(int in){industry = in;}
void set_name(string company_name){name = company_name;}
string get_name(){return name;}
string get_symbol(){return symbol;}
void set_symbol(string that){symbol = that;}
private:
double current_price;
int industry;
string name;
string symbol;
};
#endif
