# `_UINavigationBarTitleRenameRemoteView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UINavigationBarTitleRenamerContentView`
- 7 instance variables, 10 properties, 23 instance methods, 0 class methods

## Instance variables

```
{?="needsMetricsUpdate"b1} _flags;
@? _horizontalTextInsetDidChangeCallback;
d _horizontalTextInset;
q _textAlignment;
@"_UINavigationBarTitleRenamerRemoteSession" _session;
@"_UIPortalView" _portalView;
{CGSize="width"d"height"d} _intrinsicContentSize;
```

## Properties

```
@property (T@"_UINavigationBarTitleRenamerRemoteSession",R,N,V_session) session;
@property (T@"_UIPortalView",&,N,V_portalView) portalView;
@property (T{CGSize=dd},N,V_intrinsicContentSize) intrinsicContentSize;
@property (Td,N,V_horizontalTextInset) horizontalTextInset;
@property (Tq,N,V_textAlignment) textAlignment;
@property (T@?,C,N,V_horizontalTextInsetDidChangeCallback) horizontalTextInsetDidChangeCallback;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UINavigationBarTitleRenameRemoteView _connect];
-[_UINavigationBarTitleRenameRemoteView portalView];
-[_UINavigationBarTitleRenameRemoteView setTextAlignment:];
-[_UINavigationBarTitleRenameRemoteView setPortalView:];
-[_UINavigationBarTitleRenameRemoteView _disconnect];
-[_UINavigationBarTitleRenameRemoteView intrinsicContentSize];
-[_UINavigationBarTitleRenameRemoteView textAlignment];
-[_UINavigationBarTitleRenameRemoteView setIntrinsicContentSize:];
-[_UINavigationBarTitleRenameRemoteView setCenter:];
-[_UINavigationBarTitleRenameRemoteView setBounds:];
-[_UINavigationBarTitleRenameRemoteView sizeThatFits:];
-[_UINavigationBarTitleRenameRemoteView willMoveToWindow:];
-[_UINavigationBarTitleRenameRemoteView setFrame:];
-[_UINavigationBarTitleRenameRemoteView initWithSession:];
-[_UINavigationBarTitleRenameRemoteView updateMetrics];
-[_UINavigationBarTitleRenameRemoteView session];
-[_UINavigationBarTitleRenameRemoteView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:];
-[_UINavigationBarTitleRenameRemoteView horizontalTextInset];
-[_UINavigationBarTitleRenameRemoteView horizontalTextInsetDidChangeCallback];
-[_UINavigationBarTitleRenameRemoteView setHorizontalTextInset:];
-[_UINavigationBarTitleRenameRemoteView setHorizontalTextInsetDidChangeCallback:];
-[_UINavigationBarTitleRenameRemoteView setNeedsMetricsUpdate];
-[_UINavigationBarTitleRenameRemoteView updateMetricsIfNeeded];
```
