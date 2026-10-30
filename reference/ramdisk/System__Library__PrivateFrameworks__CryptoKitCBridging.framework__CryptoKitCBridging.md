# `/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging`

From the upgrade restore ramdisk (141-29011-104.dmg). 116,896 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2792)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (4 classes, 0 protocols)

Classes: `CKCBCorecryptoECPoint`, `CKCBCorecryptoECScalar`, `CKSSShare`, `SEPUtils`

## Strings (76)

```
Failed on import with share import
SEPUtils
CKSSShare
CKCBCorecryptoECScalar
CKCBCorecryptoECPoint
initWithLength:
Tr^Q,R,N,V_corecryptoScalar
dataFromACL:
group
init
initWithData:inGroup:reduction:corecryptoError:
initWithParams:x:y:
mapToCurve_SSWU_RandomOracle
y
groupOrderByteCountForCP:
initWithGeneratorForCP:
initWithx963Representation:group:
share
x
inverseModOrder
_newZeroingDataWithBytes:length:
multiply:corecryptoError:
scalarAllocationSizeForGroup:
serializedBigEndianScalar
serializedPublicKey:
initWithScalarPointer:forGroup:
_share
initWithParams:share:
initWithPublicKey:
length
mutableBytes
sub:corecryptoError:
_share_size
add:corecryptoError:
corecryptoScalar
initPoint:onGroup:
isEqual:
point
pointAllocationSizeForGroup:
x963Representation
_point
dataWithLength:
T^{ccec_cp=QQ^{cczp_funcs}[1Q]},R,N,V_group
_corecryptoScalar
T^{ccec_affine_point=[1Q]},R,N,V_point
_group
bytes
compressedx962PointByteCountForCurveParameters:
dealloc
initFromPublicKeyBytes:inGroup:compressed:corecryptoError:
initWithRandomScalarInGroup:
@32@0:8^{ccss_shamir_parameters=I{cczp=QQ^{cczp_funcs}[1Q]}}16^{ccss_shamir_share=^{cczp}I[0Q]}24
@16@0:8
^{ccss_shamir_share=^{cczp}I[0Q]}16@0:8
@32@0:8@16^{ccec_cp=QQ^{cczp_funcs}[1Q]}24
@32@0:8@16^i24
^{ccec_affine_point=[1Q]}
@24@0:8^{__SecAccessControl=}16
I16@0:8
Q24@0:8^{ccec_cp=QQ^{cczp_funcs}[1Q]}16
@32@0:8^{ccec_affine_point=[1Q]}16^{ccec_cp=QQ^{cczp_funcs}[1Q]}24
@24@0:8^{ccec_pub_ctx=^{ccec_cp}[0{ccec_projective_point=[1Q]}]}16
@36@0:8^{ccss_shamir_parameters=I{cczp=QQ^{cczp_funcs}[1Q]}}16I24@28
^{ccss_shamir_share=^{cczp}I[0Q]}
@32@0:8^Q16^{ccec_cp=QQ^{cczp_funcs}[1Q]}24
B24@0:8@16
^{ccec_cp=QQ^{cczp_funcs}[1Q]}
r^Q
^{ccec_affine_point=[1Q]}16@0:8
v16@0:8
Q
@24@0:8^{ccec_cp=QQ^{cczp_funcs}[1Q]}16
@44@0:8@16^{ccec_cp=QQ^{cczp_funcs}[1Q]}24B32^i36
^{ccec_cp=QQ^{cczp_funcs}[1Q]}16@0:8
r^Q16@0:8
@20@0:8B16
```
