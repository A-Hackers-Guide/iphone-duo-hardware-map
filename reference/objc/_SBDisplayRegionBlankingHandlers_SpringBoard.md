# `_SBDisplayRegionBlankingHandlers`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"UIWindowScene" _windowScene;
@? _beginHandler;
@? _completionHandler;
```

## Properties

```
@property (T@"UIWindowScene",R,W,N,V_windowScene) windowScene;
@property (T@?,C,N,V_beginHandler) beginHandler;
@property (T@?,C,N,V_completionHandler) completionHandler;
```

## Instance methods

```
-[_SBDisplayRegionBlankingHandlers setCompletionHandler:];
-[_SBDisplayRegionBlankingHandlers completionHandler];
-[_SBDisplayRegionBlankingHandlers windowScene];
-[_SBDisplayRegionBlankingHandlers beginHandler];
-[_SBDisplayRegionBlankingHandlers initWithWindowScene:beginHandler:completionHandler:];
-[_SBDisplayRegionBlankingHandlers setBeginHandler:];
```
