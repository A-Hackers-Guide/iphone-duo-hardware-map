# `SBDisplayPortalManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _sourceViewToPortalWindowsMap;
@"SBWindowSceneManager" _windowSceneManager;
```

## Properties

```
@property (T@"SBWindowSceneManager",R,N,V_windowSceneManager) windowSceneManager;
```

## Instance methods

```
-[SBDisplayPortalManager windowSceneManager];
-[SBDisplayPortalManager _createPortalForSourceView:sourceWindowScene:targetWindowScene:traitsRole:];
-[SBDisplayPortalManager createPortalsForSourceView:usingTraitsRole:onWindowScenesPassingTest:];
-[SBDisplayPortalManager destroyPortalsForSourceView:];
-[SBDisplayPortalManager initWithWindowSceneManager:];
```
