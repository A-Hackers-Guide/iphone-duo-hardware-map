# `CLFindMyAccessoryFirmwareUpdateManager`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<CLFindMyAccessoryFirmwareUpdateDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
{unique_ptr<CLConnectionClient, std::default_delete<CLConnectionClient>>=""{?="__ptr_"^{CLConnectionClient}}} _connection;
```

## Properties

```
@property (T@"<CLFindMyAccessoryFirmwareUpdateDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[CLFindMyAccessoryFirmwareUpdateManager handleMessage:];
-[CLFindMyAccessoryFirmwareUpdateManager init];
-[CLFindMyAccessoryFirmwareUpdateManager handleInterruption];
-[CLFindMyAccessoryFirmwareUpdateManager setDelegate:];
-[CLFindMyAccessoryFirmwareUpdateManager delegate];
-[CLFindMyAccessoryFirmwareUpdateManager initWithDelegate:delegateQueue:];
-[CLFindMyAccessoryFirmwareUpdateManager abortFirmwareUpdateForDevice:];
-[CLFindMyAccessoryFirmwareUpdateManager fetchWhetherLocalFirmwareAssetIsInUseForProductGroup:andProductNumber:];
-[CLFindMyAccessoryFirmwareUpdateManager getPersonalizationInfoForDevice:];
-[CLFindMyAccessoryFirmwareUpdateManager updateFirmwareForDevice:withAssetURL:];
-[CLFindMyAccessoryFirmwareUpdateManager useDefaultFirmwareAssetSourceForProductGroup:andProductNumber:];
-[CLFindMyAccessoryFirmwareUpdateManager useLocalFirmwareAssetFromURL:forProductGroup:forProductNumber:withSandboxExtension:];
```
