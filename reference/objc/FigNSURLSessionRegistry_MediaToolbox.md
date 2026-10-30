# `FigNSURLSessionRegistry`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _workQueue;
@"NSMutableArray" _sessionArray;
```

## Instance methods

```
-[FigNSURLSessionRegistry init];
-[FigNSURLSessionRegistry dealloc];
-[FigNSURLSessionRegistry releaseSession:];
-[FigNSURLSessionRegistry _checkForDoom:];
-[FigNSURLSessionRegistry copySessionAndAssertionForCreateOptions:dispatchQueue:outSession:outAssertion:];
```
