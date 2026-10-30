# `PKDataDetectorItem`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKDetectionItem`
- 1 instance variables, 3 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"<PKDataDetectorItemDelegate>" _delegate;
```

## Properties

```
@property (T@"<PKDataDetectorItemDelegate>",W,N,V_delegate) delegate;
@property (T@"DDScannerResult",R,N) scannerResult;
@property (T^{__DDResult=},R,N) coreResult;
```

## Class methods

```
+[PKDataDetectorItem dataDetectorItemWithQueryItem:sessionManager:];
```

## Instance methods

```
-[PKDataDetectorItem drawing];
-[PKDataDetectorItem strokeColor];
-[PKDataDetectorItem setDelegate:];
-[PKDataDetectorItem delegate];
-[PKDataDetectorItem hash];
-[PKDataDetectorItem contextMenuInteraction:willPerformPreviewActionForMenuWithConfiguration:animator:];
-[PKDataDetectorItem isEqual:];
-[PKDataDetectorItem coreResult];
-[PKDataDetectorItem scannerResult];
-[PKDataDetectorItem _baselinePath];
-[PKDataDetectorItem _highlightForView:viewTransform:drawingTransform:highlightTransform:completion:];
-[PKDataDetectorItem contextMenuInteraction:configuration:highlightPreviewInContainerView:frame:];
-[PKDataDetectorItem contextMenuInteraction:configurationForMenuAtLocation:view:identifier:];
-[PKDataDetectorItem contextMenuInteraction:configurationForMenuAtLocation:view:identifier:sourceRect:];
-[PKDataDetectorItem handleTapForMenuForInteraction:location:view:viewTransform:drawingTransform:];
-[PKDataDetectorItem handleTapForMenuForInteraction:location:view:viewTransform:drawingTransform:highlightTransform:sourceRect:];
-[PKDataDetectorItem updatedDataDetectorContextForView:sourceRect:];
```
