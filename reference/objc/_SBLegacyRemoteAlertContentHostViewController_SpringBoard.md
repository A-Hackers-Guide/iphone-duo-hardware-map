# `_SBLegacyRemoteAlertContentHostViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIRemoteViewController`
- Protocols: `SBSUIRemoteAlertItemContentHostInterface`
- 3 instance variables, 2 properties, 8 instance methods, 2 class methods

## Instance variables

```
@ _delegate;
@"NSString" _serviceClassName;
B _serviceHasSetPreferredContentSize;
```

## Properties

```
@property (T@,W,N,V_delegate) delegate;
@property (T@"NSString",C,N,V_serviceClassName) serviceClassName;
```

## Class methods

```
+[_SBLegacyRemoteAlertContentHostViewController exportedInterface];
+[_SBLegacyRemoteAlertContentHostViewController serviceViewControllerInterface];
```

## Instance methods

```
-[_SBLegacyRemoteAlertContentHostViewController viewServiceDidTerminateWithError:];
-[_SBLegacyRemoteAlertContentHostViewController _canShowWhileLocked];
-[_SBLegacyRemoteAlertContentHostViewController setDelegate:];
-[_SBLegacyRemoteAlertContentHostViewController delegate];
-[_SBLegacyRemoteAlertContentHostViewController description];
-[_SBLegacyRemoteAlertContentHostViewController serviceClassName];
-[_SBLegacyRemoteAlertContentHostViewController setServiceClassName:];
-[_SBLegacyRemoteAlertContentHostViewController _getPreferredContentSizeWithReplyBlock:];
```
