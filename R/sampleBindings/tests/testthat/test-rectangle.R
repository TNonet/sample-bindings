library('testthat')
library("sampleBindings")

test_that("RRectangle works", {
    r1 = new(RRectangle, 0, 0, 2, 2)
    
    expect_equal(r1$getArea(), 4)
    expect_equal(r1$getSize(), list(width=2, height=2))
})
