# `CTNRStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 18 instance methods, 2 class methods

## Instance variables

```
B _saSwitchVisible;
B _saSwitchConfigurable;
B _saDisabled;
B _nsaDisabled;
Q _saDisabledReasonMask;
Q _nsaDisabledReasonMask;
```

## Properties

```
@property (TB,N,GisSASwitchVisible,V_saSwitchVisible) saSwitchVisible;
@property (TB,N,GisSASwitchConfigurable,V_saSwitchConfigurable) saSwitchConfigurable;
@property (TB,N,GisSADisabled,V_saDisabled) saDisabled;
@property (TQ,N,V_saDisabledReasonMask) saDisabledReasonMask;
@property (TB,N,GisNSADisabled,V_nsaDisabled) nsaDisabled;
@property (TQ,N,V_nsaDisabledReasonMask) nsaDisabledReasonMask;
```

## Class methods

```
+[CTNRStatus supportsSecureCoding];
+[CTNRStatus default];
```

## Instance methods

```
-[CTNRStatus encodeWithCoder:];
-[CTNRStatus description];
-[CTNRStatus initWithCoder:];
-[CTNRStatus copyWithZone:];
-[CTNRStatus isEqual:];
-[CTNRStatus setNsaDisabled:];
-[CTNRStatus initWithSASwitchVisible:saSwitchConfigurable:saDisabledByBaseband:saDisabledReasonMask:nsaDisabledByBaseband:nsaDisabledReasonMask:];
-[CTNRStatus isNSADisabled];
-[CTNRStatus isSADisabled];
-[CTNRStatus isSASwitchConfigurable];
-[CTNRStatus isSASwitchVisible];
-[CTNRStatus nsaDisabledReasonMask];
-[CTNRStatus saDisabledReasonMask];
-[CTNRStatus setNsaDisabledReasonMask:];
-[CTNRStatus setSaDisabled:];
-[CTNRStatus setSaDisabledReasonMask:];
-[CTNRStatus setSaSwitchConfigurable:];
-[CTNRStatus setSaSwitchVisible:];
```
