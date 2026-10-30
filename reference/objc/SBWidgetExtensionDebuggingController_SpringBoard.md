# `SBWidgetExtensionDebuggingController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBExtensionHandling`
- 5 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"SBMainWorkspace" _workspace;
@"CHSToolSupportService" _toolService;
@"CHSWidgetExtensionProvider" _extensionProvider;
@"<SBWidgetExtensionDebugHomeScreenDataSource>" _homeScreenDataSource;
@"<SBWidgetExtensionDebugControlCenterDataSource>" _controlCenterDataSource;
```

## Properties

```
@property (T@"CHSWidgetExtensionProvider",&,N,G_extensionProvider,S_setExtensionProvider:,V_extensionProvider) extensionProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWidgetExtensionDebuggingController _extensionProvider];
-[SBWidgetExtensionDebuggingController _descriptorForWidgetFromExtension:forRequestedKind:requestedWidgetFamily:completion:];
-[SBWidgetExtensionDebuggingController _reallyFindDescriptorForWidgetFromExtension:forRequestedKind:requestedWidgetFamily:completion:];
-[SBWidgetExtensionDebuggingController _setExtensionProvider:];
-[SBWidgetExtensionDebuggingController initWithWorkspace:toolService:homeScreenDataSource:controlCenterDataSource:];
-[SBWidgetExtensionDebuggingController launchExtensionWithBundleID:options:completion:];
```
