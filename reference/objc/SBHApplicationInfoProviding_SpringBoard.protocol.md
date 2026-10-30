# `SBHApplicationInfoProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",R,N) applications;
@property (T@"NSArray",?,R,N) applicationPlaceholders;
@property (T@"NSArray",?,R,N) webClips;
```

## Instance methods

```
-[SBHApplicationInfoProviding applications];
-[SBHApplicationInfoProviding webClips];
-[SBHApplicationInfoProviding addApplicationInfoProviderObserver:];
-[SBHApplicationInfoProviding applicationPlaceholders];
-[SBHApplicationInfoProviding removeApplicationInfoProviderObserver:];
-[SBHApplicationInfoProviding uninstallApplicationWithBundleIdentifier:completion:];
```
