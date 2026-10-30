# `PKRecognitionDataCollectionViewController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UICollectionViewDelegateFlowLayout`, `UICollectionViewDataSource`, `PKHandwritingDataCollecting`
- 7 instance variables, 12 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _drawings;
@"NSArray" _drawingImages;
@"NSDictionary" _metadata;
@"UIScrollView" _scrollView;
@"UILabel" _descriptionLabel;
@"UICollectionView" _collectionView;
@"NSLayoutConstraint" _collectionViewHeightConstraint;
```

## Properties

```
@property (T@"NSArray",&,N,V_drawings) drawings;
@property (T@"NSArray",&,N,V_drawingImages) drawingImages;
@property (T@"NSDictionary",&,N,V_metadata) metadata;
@property (T@"UIScrollView",&,N,V_scrollView) scrollView;
@property (T@"UILabel",&,N,V_descriptionLabel) descriptionLabel;
@property (T@"UICollectionView",&,N,V_collectionView) collectionView;
@property (T@"NSLayoutConstraint",&,N,V_collectionViewHeightConstraint) collectionViewHeightConstraint;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIViewController",R) viewController;
```

## Instance methods

```
-[PKRecognitionDataCollectionViewController setDescriptionLabel:];
-[PKRecognitionDataCollectionViewController descriptionLabel];
-[PKRecognitionDataCollectionViewController collectionView:numberOfItemsInSection:];
-[PKRecognitionDataCollectionViewController collectionView:didSelectItemAtIndexPath:];
-[PKRecognitionDataCollectionViewController scrollView];
-[PKRecognitionDataCollectionViewController collectionView:cellForItemAtIndexPath:];
-[PKRecognitionDataCollectionViewController collectionView];
-[PKRecognitionDataCollectionViewController viewDidLoad];
-[PKRecognitionDataCollectionViewController setScrollView:];
-[PKRecognitionDataCollectionViewController viewDidLayoutSubviews];
-[PKRecognitionDataCollectionViewController metadata];
-[PKRecognitionDataCollectionViewController viewController];
-[PKRecognitionDataCollectionViewController setCollectionView:];
-[PKRecognitionDataCollectionViewController setMetadata:];
-[PKRecognitionDataCollectionViewController collectionViewHeightConstraint];
-[PKRecognitionDataCollectionViewController setCollectionViewHeightConstraint:];
-[PKRecognitionDataCollectionViewController adjustCollectionViewHeight];
-[PKRecognitionDataCollectionViewController drawingImages];
-[PKRecognitionDataCollectionViewController drawings];
-[PKRecognitionDataCollectionViewController initWithDrawings:metadata:];
-[PKRecognitionDataCollectionViewController saveDataForDrawings:baseURL:shouldSaveRecognitionData:];
-[PKRecognitionDataCollectionViewController setDrawingImages:];
-[PKRecognitionDataCollectionViewController setDrawings:];
-[PKRecognitionDataCollectionViewController submitFeedback];
-[PKRecognitionDataCollectionViewController synchronousImageForDrawing:];
```
