# `WFHotspotDetailsView`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIStackView`
- 6 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
Q _batteryCharge;
@"NSString" _cellularProtocolString;
Q _signalBars;
@"_UIBatteryView" _batteryView;
@"UIImageView" _signalImageView;
@"UILabel" _networkTypeLabel;
```

## Properties

```
@property (T@"_UIBatteryView",&,N,V_batteryView) batteryView;
@property (T@"UIImageView",&,N,V_signalImageView) signalImageView;
@property (T@"UILabel",&,N,V_networkTypeLabel) networkTypeLabel;
@property (TQ,N,V_batteryCharge) batteryCharge;
@property (T@"NSString",C,N,V_cellularProtocolString) cellularProtocolString;
@property (TQ,N,V_signalBars) signalBars;
```

## Instance methods

```
-[WFHotspotDetailsView signalBars];
-[WFHotspotDetailsView intrinsicContentSize];
-[WFHotspotDetailsView setBatteryView:];
-[WFHotspotDetailsView setSignalBars:];
-[WFHotspotDetailsView batteryView];
-[WFHotspotDetailsView initWithCoder:];
-[WFHotspotDetailsView initWithFrame:];
-[WFHotspotDetailsView setupSubviews];
-[WFHotspotDetailsView batteryCharge];
-[WFHotspotDetailsView setBatteryCharge:];
-[WFHotspotDetailsView cellularProtocolString];
-[WFHotspotDetailsView signalImageView];
-[WFHotspotDetailsView attributedStringFromCellularProtocol:];
-[WFHotspotDetailsView networkTypeLabel];
-[WFHotspotDetailsView setCellularProtocolString:];
-[WFHotspotDetailsView setNetworkTypeLabel:];
-[WFHotspotDetailsView setSignalImageView:];
-[WFHotspotDetailsView updateCellularProtocolLabel];
-[WFHotspotDetailsView updateSignalBars];
```
