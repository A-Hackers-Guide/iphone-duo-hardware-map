# `BKHIDEventProcessorCreationContext`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"<BKHIDSystemInterfacing>" _systemInterface;
@"<BKHIDEventDispatcher>" _eventDispatcher;
@"<BKIOHIDServiceMatcherDataProviding>" _serviceMatcherDataProvider;
@"<BKHIDEventProcessorRegistering>" _eventProcessorRegistry;
@"<BKDisplayRenderSpace>" _displayRenderSpace;
@"<BKOrientationProvider>" _orientationProvider;
@"<BKHIDEventDeliveryManagerProviding>" _deliveryManagerProvider;
@"BKTouchDeliveryObservationManager" _deliveryObservationManager;
@"BKTouchPadManager" _touchPadManager;
# _keyboardHIDEventProcessorClass;
# _smartCoverHIDEventProcessorClass;
@"BKHIDUISensorCoordinator" _sensorCoordinator;
@"BKTouchDeliveryObservationManager" _touchDeliveryObservationManager;
```

## Properties

```
@property (T@"<BKHIDSystemInterfacing>",&,N,V_systemInterface) systemInterface;
@property (T@"<BKHIDEventDispatcher>",&,N,V_eventDispatcher) eventDispatcher;
@property (T@"<BKIOHIDServiceMatcherDataProviding>",&,N,V_serviceMatcherDataProvider) serviceMatcherDataProvider;
@property (T@"<BKHIDEventProcessorRegistering>",&,N,V_eventProcessorRegistry) eventProcessorRegistry;
@property (T@"<BKDisplayRenderSpace>",&,N,V_displayRenderSpace) displayRenderSpace;
@property (T@"<BKOrientationProvider>",&,N,V_orientationProvider) orientationProvider;
@property (T@"<BKHIDEventDeliveryManagerProviding>",&,N,V_deliveryManagerProvider) deliveryManagerProvider;
@property (T@"BKTouchPadManager",&,N,V_touchPadManager) touchPadManager;
@property (T@"BKTouchDeliveryObservationManager",&,N,V_touchDeliveryObservationManager) touchDeliveryObservationManager;
@property (T#,&,N,V_keyboardHIDEventProcessorClass) keyboardHIDEventProcessorClass;
@property (T#,&,N,V_smartCoverHIDEventProcessorClass) smartCoverHIDEventProcessorClass;
@property (T@"BKHIDUISensorCoordinator",&,N,V_sensorCoordinator) sensorCoordinator;
@property (T@"BKTouchDeliveryObservationManager",R,N,V_deliveryObservationManager) deliveryObservationManager;
```

## Instance methods

```
-[BKHIDEventProcessorCreationContext eventDispatcher];
-[BKHIDEventProcessorCreationContext setOrientationProvider:];
-[BKHIDEventProcessorCreationContext touchPadManager];
-[BKHIDEventProcessorCreationContext setTouchPadManager:];
-[BKHIDEventProcessorCreationContext setEventDispatcher:];
-[BKHIDEventProcessorCreationContext orientationProvider];
-[BKHIDEventProcessorCreationContext setDisplayRenderSpace:];
-[BKHIDEventProcessorCreationContext displayRenderSpace];
-[BKHIDEventProcessorCreationContext deliveryObservationManager];
-[BKHIDEventProcessorCreationContext sensorCoordinator];
-[BKHIDEventProcessorCreationContext setSensorCoordinator:];
-[BKHIDEventProcessorCreationContext systemInterface];
-[BKHIDEventProcessorCreationContext touchDeliveryObservationManager];
-[BKHIDEventProcessorCreationContext deliveryManagerProvider];
-[BKHIDEventProcessorCreationContext eventProcessorRegistry];
-[BKHIDEventProcessorCreationContext keyboardHIDEventProcessorClass];
-[BKHIDEventProcessorCreationContext serviceMatcherDataProvider];
-[BKHIDEventProcessorCreationContext setDeliveryManagerProvider:];
-[BKHIDEventProcessorCreationContext setEventProcessorRegistry:];
-[BKHIDEventProcessorCreationContext setKeyboardHIDEventProcessorClass:];
-[BKHIDEventProcessorCreationContext setServiceMatcherDataProvider:];
-[BKHIDEventProcessorCreationContext setSmartCoverHIDEventProcessorClass:];
-[BKHIDEventProcessorCreationContext setSystemInterface:];
-[BKHIDEventProcessorCreationContext setTouchDeliveryObservationManager:];
-[BKHIDEventProcessorCreationContext smartCoverHIDEventProcessorClass];
```
