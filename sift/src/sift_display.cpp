#include <iostream>
#include "opencv2/core.hpp"
#ifdef HAVE_OPENCV_XFEATURES2D
#include "opencv2/highgui.hpp"
#include "opencv2/features2d.hpp"
#include "opencv2/xfeatures2d.hpp"
#include <fstream>
#include <algorithm>
using namespace cv;
using namespace cv::xfeatures2d;
using std::cout;
using std::endl;
int main( int argc, char* argv[] )
{
    CommandLineParser parser( argc, argv, "{@input | box.png | input image}" );
    Mat src = imread( samples::findFile( parser.get<String>( "@input" ) ) );



    std::cout << "directory_iterator:\n";


    //Mat src = imread( samples::findFile( parser.get<String>( "@input" ) ), IMREAD_GRAYSCALE );
    if ( src.empty() )
    {
        cout << "Could not open or find the image!\n" << endl;
        cout << "Usage: " << argv[0] << " <Input image>" << endl;
        return -1;
    }
    //-- Step 1: Detect the keypoints using SURF Detector
    int nfeatures = 400;
    Ptr<SIFT> detector = SIFT::create(nfeatures = nfeatures);
    std::vector<KeyPoint> keypoints;

    for(auto it = keypoints.begin(); it != keypoints.end(); it++ ){
	cout << (*it).pt << endl;
    }

    detector->detect( src, keypoints );
    //-- Draw keypoints
    Mat img_keypoints;
    drawKeypoints( src, keypoints, img_keypoints );
    //-- Show detected (drawn) keypoints

    cout << "showing the image"<<endl;
    //imshow("SIFT Keypoints", img_keypoints );
    //waitKey();
    imwrite("worstskin.png", img_keypoints);
    return 0;
}
#else
int main()
{
    std::cout << "This tutorial code needs the xfeatures2d contrib module to be run." << std::endl;
    return 0;
}
#endif
