# `DSRemoteUILoader`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AAUIGrandSlamRemoteUIPresenterDelegate`, `AIDAAccountManagerDelegate`, `DSController`
- 6 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"AIDAAccountManager" _accountManager;
@"ACAccount" _currentAccount;
@"AAUIGrandSlamRemoteUIPresenter" _privacyRepairPresenter;
@"IDSIDQueryController" _queryController;
@"NSURL" _dynamicURL;
@"<DSNavigationDelegate>" _delegate;
```

## Properties

```
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSRemoteUILoader initialize];
```

## Instance methods

```
-[DSRemoteUILoader setDelegate:];
-[DSRemoteUILoader delegate];
-[DSRemoteUILoader remoteUIDidReceiveHTTPResponse:];
-[DSRemoteUILoader accountsForAccountManager:];
-[DSRemoteUILoader remoteUIDidEndFlow:];
-[DSRemoteUILoader remoteUIRequestComplete:error:];
-[DSRemoteUILoader remoteUIWillLoadRequest:];
-[DSRemoteUILoader remoteUIWillPresentObjectModel:modally:];
-[DSRemoteUILoader initWithPresenter:delegate:URL:];
-[DSRemoteUILoader initWithAccountManager:presenter:delegate:];
-[DSRemoteUILoader initWithPresenter:delegate:];
-[DSRemoteUILoader loadRemoteUI];
-[DSRemoteUILoader loadRemoteUIFromURL:];
```
