# `DCImageAnalyzerManager`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 3 instance methods, 2 class methods

## Instance variables

```
@"VKCImageAnalyzer" _imageAnalyzer;
@"NSCache" _cachedAnalyses;
@"NSObject<OS_dispatch_queue>" _operationQueue;
```

## Class methods

```
+[DCImageAnalyzerManager sharedInstance];
+[DCImageAnalyzerManager isImageAnalysisEnabled];
```

## Instance methods

```
-[DCImageAnalyzerManager cleanup];
-[DCImageAnalyzerManager init];
-[DCImageAnalyzerManager analysisForImage:completionHandler:];
```
