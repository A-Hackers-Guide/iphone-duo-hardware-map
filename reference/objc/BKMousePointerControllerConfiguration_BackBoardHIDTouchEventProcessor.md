# `BKMousePointerControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 19 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _displayLinkDisabled;
B _shouldUseHighFrequencyAttributeOption;
@"<BKCADisplayProvider>" _displayProvider;
@"<BKOrientationProvider>" _orientationProvider;
@"BKTouchPadManager" _touchPadManager;
@"<BKSmartCoverObserving>" _smartCoverEventProcessor;
@"<BKGlobalKeyboardEventObserving>" _keyboardEventProcessor;
@"BKHIDEventDeliveryManager" _eventDeliveryManager;
@"<BKDisplayRenderSpace>" _displayRenderSpace;
@"<BKHIDSystemInterfacing>" _systemInterfaceProvider;
@"BKSLocalDefaults" _localDefaults;
@"BKHIDClientConnectionManager" _clientConnectionManager;
@"BKMousePointerAnalyticsReporter" _analyticsReporter;
@"BKMousePointerServiceServer" _serviceServer;
@"BKTouchDeliveryPolicyServer" _touchDeliveryPolicyServer;
@"<BKHIDEventHitTestDispatcher>" _eventDispatcher;
# _displayLinkClass;
d _mainDisplayCornerRadius;
@"BKDisplayOrientationController" _displayOrientationController;
```

## Properties

```
@property (T@"<BKCADisplayProvider>",&,N,V_displayProvider) displayProvider;
@property (T@"<BKOrientationProvider>",&,N,V_orientationProvider) orientationProvider;
@property (T@"BKTouchPadManager",&,N,V_touchPadManager) touchPadManager;
@property (T@"<BKSmartCoverObserving>",&,N,V_smartCoverEventProcessor) smartCoverEventProcessor;
@property (T@"<BKGlobalKeyboardEventObserving>",&,N,V_keyboardEventProcessor) keyboardEventProcessor;
@property (T@"BKHIDEventDeliveryManager",&,N,V_eventDeliveryManager) eventDeliveryManager;
@property (T@"<BKDisplayRenderSpace>",&,N,V_displayRenderSpace) displayRenderSpace;
@property (T@"<BKHIDSystemInterfacing>",&,N,V_systemInterfaceProvider) systemInterfaceProvider;
@property (T@"BKSLocalDefaults",&,N,V_localDefaults) localDefaults;
@property (T@"BKHIDClientConnectionManager",&,N,V_clientConnectionManager) clientConnectionManager;
@property (T@"BKMousePointerAnalyticsReporter",&,N,V_analyticsReporter) analyticsReporter;
@property (T@"BKMousePointerServiceServer",&,N,V_serviceServer) serviceServer;
@property (T@"BKTouchDeliveryPolicyServer",&,N,V_touchDeliveryPolicyServer) touchDeliveryPolicyServer;
@property (T@"<BKHIDEventHitTestDispatcher>",&,N,V_eventDispatcher) eventDispatcher;
@property (T#,&,N,V_displayLinkClass) displayLinkClass;
@property (TB,N,V_displayLinkDisabled) displayLinkDisabled;
@property (TB,N,V_shouldUseHighFrequencyAttributeOption) shouldUseHighFrequencyAttributeOption;
@property (Td,N,V_mainDisplayCornerRadius) mainDisplayCornerRadius;
@property (T@"BKDisplayOrientationController",&,N,V_displayOrientationController) displayOrientationController;
```

## Instance methods

```
-[BKMousePointerControllerConfiguration eventDispatcher];
-[BKMousePointerControllerConfiguration setOrientationProvider:];
-[BKMousePointerControllerConfiguration touchPadManager];
-[BKMousePointerControllerConfiguration smartCoverEventProcessor];
-[BKMousePointerControllerConfiguration setClientConnectionManager:];
-[BKMousePointerControllerConfiguration touchDeliveryPolicyServer];
-[BKMousePointerControllerConfiguration setTouchDeliveryPolicyServer:];
-[BKMousePointerControllerConfiguration setAnalyticsReporter:];
-[BKMousePointerControllerConfiguration setTouchPadManager:];
-[BKMousePointerControllerConfiguration setDisplayLinkClass:];
-[BKMousePointerControllerConfiguration setDisplayOrientationController:];
-[BKMousePointerControllerConfiguration setEventDeliveryManager:];
-[BKMousePointerControllerConfiguration displayOrientationController];
-[BKMousePointerControllerConfiguration mainDisplayCornerRadius];
-[BKMousePointerControllerConfiguration setEventDispatcher:];
-[BKMousePointerControllerConfiguration analyticsReporter];
-[BKMousePointerControllerConfiguration displayLinkDisabled];
-[BKMousePointerControllerConfiguration clientConnectionManager];
-[BKMousePointerControllerConfiguration setDisplayLinkDisabled:];
-[BKMousePointerControllerConfiguration orientationProvider];
-[BKMousePointerControllerConfiguration displayProvider];
-[BKMousePointerControllerConfiguration setServiceServer:];
-[BKMousePointerControllerConfiguration setSmartCoverEventProcessor:];
-[BKMousePointerControllerConfiguration shouldUseHighFrequencyAttributeOption];
-[BKMousePointerControllerConfiguration displayLinkClass];
-[BKMousePointerControllerConfiguration eventDeliveryManager];
-[BKMousePointerControllerConfiguration localDefaults];
-[BKMousePointerControllerConfiguration setDisplayRenderSpace:];
-[BKMousePointerControllerConfiguration keyboardEventProcessor];
-[BKMousePointerControllerConfiguration setKeyboardEventProcessor:];
-[BKMousePointerControllerConfiguration setDisplayProvider:];
-[BKMousePointerControllerConfiguration setLocalDefaults:];
-[BKMousePointerControllerConfiguration displayRenderSpace];
-[BKMousePointerControllerConfiguration setSystemInterfaceProvider:];
-[BKMousePointerControllerConfiguration systemInterfaceProvider];
-[BKMousePointerControllerConfiguration serviceServer];
-[BKMousePointerControllerConfiguration setMainDisplayCornerRadius:];
-[BKMousePointerControllerConfiguration setShouldUseHighFrequencyAttributeOption:];
```
