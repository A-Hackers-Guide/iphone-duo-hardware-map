# `UIRemoteInputViewInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _shouldShowDockView;
i _processId;
I _contextId;
{CGSize="width"d"height"d} _size;
{NSEdgeInsets="top"d"left"d"bottom"d"right"d} _insets;
```

## Properties

```
@property (T{CGSize=dd},N,V_size) size;
@property (T{NSEdgeInsets=dddd},N,V_insets) insets;
@property (Ti,N,V_processId) processId;
@property (TI,N,V_contextId) contextId;
@property (TB,N,V_shouldShowDockView) shouldShowDockView;
@property (T@"RTIInputViewInfo",R,N) rtiInputViewInfo;
```

## Instance methods

```
-[UIRemoteInputViewInfo setProcessId:];
-[UIRemoteInputViewInfo contextId];
-[UIRemoteInputViewInfo setContextId:];
-[UIRemoteInputViewInfo processId];
-[UIRemoteInputViewInfo setShouldShowDockView:];
-[UIRemoteInputViewInfo size];
-[UIRemoteInputViewInfo shouldShowDockView];
-[UIRemoteInputViewInfo description];
-[UIRemoteInputViewInfo setSize:];
-[UIRemoteInputViewInfo insets];
-[UIRemoteInputViewInfo rtiInputViewInfo];
-[UIRemoteInputViewInfo setInsets:];
```
