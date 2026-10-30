# `_UINavigationBarTitleRenamer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 16 instance methods, 1 class methods

## Instance variables

```
{?="allowsMultipleSessions"b1} _flags;
@"<_UINavigationBarTitleRenamerDelegate>" _delegate;
@"NSMutableSet" _trackedSessions;
```

## Properties

```
@property (T@"NSMutableSet",R,N,V_trackedSessions) trackedSessions;
@property (T@"<_UINavigationBarTitleRenamerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[_UINavigationBarTitleRenamer renameServer];
```

## Instance methods

```
-[_UINavigationBarTitleRenamer init];
-[_UINavigationBarTitleRenamer dealloc];
-[_UINavigationBarTitleRenamer setDelegate:];
-[_UINavigationBarTitleRenamer startSession:];
-[_UINavigationBarTitleRenamer delegate];
-[_UINavigationBarTitleRenamer description];
-[_UINavigationBarTitleRenamer endSession:];
-[_UINavigationBarTitleRenamer _sessionTextFieldDidEndEditing:];
-[_UINavigationBarTitleRenamer trackedSessions];
-[_UINavigationBarTitleRenamer _session:fileRenameDidEnd:];
-[_UINavigationBarTitleRenamer _session:fileRenameDidFail:];
-[_UINavigationBarTitleRenamer _session:textFieldShouldEndRenamingWithTitle:];
-[_UINavigationBarTitleRenamer _session:textFieldWillBeginRenamingWithTitle:selectedRange:];
-[_UINavigationBarTitleRenamer _sessionDidCancel:];
-[_UINavigationBarTitleRenamer sceneWillDeactivateNotification:];
-[_UINavigationBarTitleRenamer sessionWithIdentifier:];
```
