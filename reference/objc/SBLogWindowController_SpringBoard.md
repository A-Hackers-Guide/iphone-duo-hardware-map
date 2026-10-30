# `SBLogWindowController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 2 instance variables, 2 properties, 8 instance methods, 4 class methods

## Instance variables

```
@"UITextView" _logTextView;
@"SBWindow" _logWindow;
```

## Properties

```
@property (T@"SBWindow",&,N,V_logWindow) logWindow;
@property (T@"UITextView",&,N,V_logTextView) logTextView;
```

## Class methods

```
+[SBLogWindowController sharedInstance];
+[SBLogWindowController setWindowScene:];
+[SBLogWindowController windowScene];
+[SBLogWindowController sharedInstanceIfAvailable];
```

## Instance methods

```
-[SBLogWindowController hide];
-[SBLogWindowController initWithNibName:bundle:];
-[SBLogWindowController show];
-[SBLogWindowController setLogTextView:];
-[SBLogWindowController _createAndUpdateWindowIfNecessary];
-[SBLogWindowController logTextView];
-[SBLogWindowController logWindow];
-[SBLogWindowController setLogWindow:];
```
