# `WFPrivateAddressModeOptionsViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFValueListViewController`
- 5 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _isCurrentNetwork;
B _isChinaDevice;
@"NSString" _originalSelection;
@"NSString" _pendingSelection;
@"NSString" _networkName;
```

## Properties

```
@property (T@"NSString",C,N,V_originalSelection) originalSelection;
@property (T@"NSString",C,N,V_pendingSelection) pendingSelection;
@property (TB,N,V_isCurrentNetwork) isCurrentNetwork;
@property (T@"NSString",C,N,V_networkName) networkName;
@property (TB,N,V_isChinaDevice) isChinaDevice;
```

## Instance methods

```
-[WFPrivateAddressModeOptionsViewController networkName];
-[WFPrivateAddressModeOptionsViewController tableView:didSelectRowAtIndexPath:];
-[WFPrivateAddressModeOptionsViewController isChinaDevice];
-[WFPrivateAddressModeOptionsViewController setNetworkName:];
-[WFPrivateAddressModeOptionsViewController setPendingSelection:];
-[WFPrivateAddressModeOptionsViewController isCurrentNetwork];
-[WFPrivateAddressModeOptionsViewController setIsChinaDevice:];
-[WFPrivateAddressModeOptionsViewController _promptForAllowTrackingCurrentNetwork:indexPath:];
-[WFPrivateAddressModeOptionsViewController _promptForInterruptCurrentNetwork:];
-[WFPrivateAddressModeOptionsViewController initWithTitles:originalSelection:isCurrentNetwork:currentNetworkName:isChinaDevice:];
-[WFPrivateAddressModeOptionsViewController originalSelection];
-[WFPrivateAddressModeOptionsViewController pendingSelection];
-[WFPrivateAddressModeOptionsViewController setIsCurrentNetwork:];
-[WFPrivateAddressModeOptionsViewController setOriginalSelection:];
```
