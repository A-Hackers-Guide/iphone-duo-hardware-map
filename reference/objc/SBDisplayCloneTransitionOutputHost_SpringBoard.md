# `SBDisplayCloneTransitionOutputHost`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayCloneTransitionOutputHosting`
- 1 instance variables, 4 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _activeOutputWindows;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBDisplayCloneTransitionOutputHost outputWindowLevelForSourceWindowLevel:];
```

## Instance methods

```
-[SBDisplayCloneTransitionOutputHost init];
-[SBDisplayCloneTransitionOutputHost _tearDownOutputWindow:];
-[SBDisplayCloneTransitionOutputHost hostTransitionOutputView:aboveSourceView:onWindowScene:];
```
