#include <Rcpp.h>
#include <src/include/Rectangle.h>


class RRectanlge : public shapes::Rectangle{
    public:
        // Default constructor
        RRectanlge () {}
        
        // Overloaded constructor
        RRectanlge (int x0, int y0, int x1, int y1) : shapes::Rectangle(x0, y0, x1, y1) {}
        
        Rcpp::List getSize_R(){
            int width;
            int height;
            this->getSize(&width, &height);
            return Rcpp::List::create(Rcpp::Named("width") = width,
                                      Rcpp::Named("height") = height);
            
        }

};


RCPP_MODULE(rectangle) {
    Rcpp::class_<shapes::Rectangle>("Rectangle")
        .constructor()
        .constructor<int, int, int, int>("overloaded constructor")
        .method("getArea", &shapes::Rectangle::getArea, "get area of Rectangle")
        .method("move", &shapes::Rectangle::move, "move rectangle")
        .field("x0", &shapes::Rectangle::x0)
        .field("x1", &shapes::Rectangle::x1)
        .field("y0", &shapes::Rectangle::y0)
        .field("y1", &shapes::Rectangle::y1)
    ;

    Rcpp::class_<RRectanlge>("RRectangle")
        .derives<shapes::Rectangle>("Rectangle")
        .constructor()
        .constructor<int, int, int, int>("overloaded constructor")
        .method("getSize", &RRectanlge::getSize_R, "get size of Rectangle")
    ;
}
