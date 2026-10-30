# `DCSettings`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 7 properties, 21 instance methods, 3 class methods

## Instance variables

```
@"NSUserDefaults" _userDefaults;
```

## Properties

```
@property (T@"NSUserDefaults",&,V_userDefaults) userDefaults;
@property (TB,R,N) enableViewService;
@property (TB,R,N) finishAfterFirstScan;
@property (TB,R,N) useDocumentSegmentationRequest;
@property (TB,R,N) enableWindex;
@property (TB,R,N) videoGravityPrefersAspectFitForResizablePhoneLayout;
@property (Td,R,N) imageQuality;
```

## Class methods

```
+[DCSettings sharedSettings];
+[DCSettings _isSolariumEnabled];
+[DCSettings _usesStandardNavigationBar];
```

## Instance methods

```
-[DCSettings userDefaults];
-[DCSettings init];
-[DCSettings setUserDefaults:];
-[DCSettings enableViewService];
-[DCSettings enableViewServiceBoxed];
-[DCSettings enableWindex];
-[DCSettings enableWindexBoxed];
-[DCSettings finishAfterFirstScan];
-[DCSettings finishAfterFirstScanBoxed];
-[DCSettings imageQuality];
-[DCSettings imageQualityBoxed];
-[DCSettings setEnableViewServiceBoxed:];
-[DCSettings setEnableWindexBoxed:];
-[DCSettings setFinishAfterFirstScanBoxed:];
-[DCSettings setImageQualityBoxed:];
-[DCSettings setUseDocumentSegmentationRequestBoxed:];
-[DCSettings setVideoGravityPrefersAspectFitForResizablePhoneLayoutBoxed:];
-[DCSettings useDocumentSegmentationRequest];
-[DCSettings useDocumentSegmentationRequestBoxed];
-[DCSettings videoGravityPrefersAspectFitForResizablePhoneLayout];
-[DCSettings videoGravityPrefersAspectFitForResizablePhoneLayoutBoxed];
```
