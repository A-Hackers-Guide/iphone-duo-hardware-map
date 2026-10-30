# `AVPointCloudData`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 10 properties, 14 instance methods, 1 class methods

## Instance variables

```
^{__CVBuffer=} _dataBuffer;
q _projectorMode;
@"ADJasperPointCloud" _jasperPointCloud;
```

## Properties

```
@property (T@"ADJasperPointCloud",R,&,N) jasperPointCloud;
@property (TI,R) pointCloudFormatType;
@property (Tq,R) pointCount;
@property (Tr^,R) points;
@property (Tr^f,R) confidenceScores;
@property (Tr^,R) pointsAndConfidenceScores;
@property (Tr*,R) spotIdentifiers;
@property (Tr*,R) bankIdentifiers;
@property (T^{__CVBuffer=},R) pointCloudDataBuffer;
@property (Tq,R) projectorMode;
```

## Class methods

```
+[AVPointCloudData initialize];
```

## Instance methods

```
-[AVPointCloudData pointCount];
-[AVPointCloudData debugDescription];
-[AVPointCloudData dealloc];
-[AVPointCloudData projectorMode];
-[AVPointCloudData description];
-[AVPointCloudData points];
-[AVPointCloudData confidenceScores];
-[AVPointCloudData spotIdentifiers];
-[AVPointCloudData bankIdentifiers];
-[AVPointCloudData initWithDataBuffer:];
-[AVPointCloudData jasperPointCloud];
-[AVPointCloudData pointCloudDataBuffer];
-[AVPointCloudData pointCloudFormatType];
-[AVPointCloudData pointsAndConfidenceScores];
```
