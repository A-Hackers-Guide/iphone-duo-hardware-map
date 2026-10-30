# `PLButtonAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 7 instance variables, 7 properties, 23 instance methods, 11 class methods

## Instance variables

```
@"PLXPCListenerOperatorComposition" _captureButtonActionListener;
@"PLXPCListenerOperatorComposition" _buttonSelectionListener;
@"PLXPCListenerOperatorComposition" _buttonSelectionChangedListener;
@"PLXPCListenerOperatorComposition" _buttonInteractionListener;
@"PLEntryNotificationOperatorComposition" _batteryLevelChanged;
@"PLHIDEventOperatorComposition" _buttonEvent;
@"PLHIDEventOperatorComposition" _smartCoverEvent;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_captureButtonActionListener) captureButtonActionListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_buttonSelectionListener) buttonSelectionListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_buttonSelectionChangedListener) buttonSelectionChangedListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_buttonInteractionListener) buttonInteractionListener;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChanged) batteryLevelChanged;
@property (T@"PLHIDEventOperatorComposition",&,V_buttonEvent) buttonEvent;
@property (T@"PLHIDEventOperatorComposition",&,V_smartCoverEvent) smartCoverEvent;
```

## Class methods

```
+[PLButtonAgent entryEventIntervalDefinitions];
+[PLButtonAgent entryEventPointDefinitions];
+[PLButtonAgent entryEventForwardDefinitions];
+[PLButtonAgent entryEventBackwardDefinitions];
+[PLButtonAgent entryEventNoneDefinitions];
+[PLButtonAgent load];
+[PLButtonAgent defaults];
+[PLButtonAgent entryAggregateDefinitions];
+[PLButtonAgent entryEventBackwardDefinitionTrackpadPowerState];
+[PLButtonAgent entryEventForwardDefinitionActionButtonInteraction];
+[PLButtonAgent entryEventForwardDefinitionActionButtonSelection];
```

## Instance methods

```
-[PLButtonAgent setButtonSelectionChangedListener:];
-[PLButtonAgent logEventForwardActionButtonInteraction:];
-[PLButtonAgent logEventForwardSmartCover:];
-[PLButtonAgent buttonInteractionListener];
-[PLButtonAgent captureButtonActionListener];
-[PLButtonAgent init];
-[PLButtonAgent setButtonEvent:];
-[PLButtonAgent initOperatorDependancies];
-[PLButtonAgent setSmartCoverEvent:];
-[PLButtonAgent setButtonInteractionListener:];
-[PLButtonAgent setButtonSelectionListener:];
-[PLButtonAgent interactionTypeStringToEnum:];
-[PLButtonAgent logEventForwardActionButtonSelection:];
-[PLButtonAgent smartCoverEvent];
-[PLButtonAgent logEventPointButton:];
-[PLButtonAgent logEventBackwardCaptureButtonAction:];
-[PLButtonAgent buttonSelectionChangedListener];
-[PLButtonAgent setBatteryLevelChanged:];
-[PLButtonAgent log];
-[PLButtonAgent buttonSelectionListener];
-[PLButtonAgent batteryLevelChanged];
-[PLButtonAgent buttonEvent];
-[PLButtonAgent setCaptureButtonActionListener:];
```
