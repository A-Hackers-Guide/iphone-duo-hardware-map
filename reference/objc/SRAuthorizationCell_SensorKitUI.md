# `SRAuthorizationCell`

- Image: [`/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI`](../userland/System__Library__PrivateFrameworks__SensorKitUI.framework__SensorKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCell`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"UISwitch" _toggle;
@"NSIndexPath" _indexPath;
@"<SRAuthorizationCellDelegate>" _delegate;
```

## Properties

```
@property (T@"UISwitch",&,N,V_toggle) toggle;
@property (T@"NSIndexPath",&,N,V_indexPath) indexPath;
@property (T@"<SRAuthorizationCellDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[SRAuthorizationCell authorizationCellForIndexPath:title:state:delegate:tableView:];
```

## Instance methods

```
-[SRAuthorizationCell indexPath];
-[SRAuthorizationCell dealloc];
-[SRAuthorizationCell setDelegate:];
-[SRAuthorizationCell setIndexPath:];
-[SRAuthorizationCell delegate];
-[SRAuthorizationCell initWithStyle:reuseIdentifier:];
-[SRAuthorizationCell setToggle:];
-[SRAuthorizationCell toggle];
-[SRAuthorizationCell switchChanged];
```
