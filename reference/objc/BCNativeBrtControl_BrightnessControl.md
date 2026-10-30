# `BCNativeBrtControl`

- Image: [`/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`](../userland/System__Library__PrivateFrameworks__BrightnessControl.framework__BrightnessControl.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BCBrtControl`
- 4 instance variables, 0 properties, 13 instance methods, 5 class methods

## Instance variables

```
@"<CBPrimitiveConfigurationProvider>" _provider;
@"<CBPrimitiveConfigurationProvider>" _iomfbProvider;
I _backlightService;
@"NSString" _dcpRole;
```

## Class methods

```
+[BCNativeBrtControl copyAvailableControls];
+[BCNativeBrtControl newMonitorWithHandler:error:];
+[BCNativeBrtControl parseAABCapCurve:];
+[BCNativeBrtControl parseEDRCapabilities:];
+[BCNativeBrtControl parsePanelLimits:toCapabilities:ignoreLmidCalibration:];
```

## Instance methods

```
-[BCNativeBrtControl ID];
-[BCNativeBrtControl dealloc];
-[BCNativeBrtControl description];
-[BCNativeBrtControl registryID];
-[BCNativeBrtControl initWithService:];
-[BCNativeBrtControl minNits];
-[BCNativeBrtControl parsePAABFromProvider:andIOMFB:];
-[BCNativeBrtControl maxNits];
-[BCNativeBrtControl copyModuleIdentifier];
-[BCNativeBrtControl parseCapabilities:withDCPEndpoint:andError:];
-[BCNativeBrtControl parseColorAdaptationCapabilities:];
-[BCNativeBrtControl setDisplayService:];
-[BCNativeBrtControl setNits:error:];
```
