# `SBFFileCacheURLFaultHandler`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFFileCacheFaultHandler`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _retryIntervals;
@"NSURLSession" _urlSession;
```

## Properties

```
@property (T@"NSURLSession",&,V_urlSession) urlSession;
@property (T@"NSArray",C,V_retryIntervals) retryIntervals;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFFileCacheURLFaultHandler init];
-[SBFFileCacheURLFaultHandler urlSession];
-[SBFFileCacheURLFaultHandler setUrlSession:];
-[SBFFileCacheURLFaultHandler attemptLoadFromURL:session:retryIntervalEnumerator:completionHandler:];
-[SBFFileCacheURLFaultHandler fileCache:loadFileForIdentifier:completionHandler:];
-[SBFFileCacheURLFaultHandler performLoadFromURL:session:completionHandler:];
-[SBFFileCacheURLFaultHandler retryIntervals];
-[SBFFileCacheURLFaultHandler setRetryIntervals:];
```
