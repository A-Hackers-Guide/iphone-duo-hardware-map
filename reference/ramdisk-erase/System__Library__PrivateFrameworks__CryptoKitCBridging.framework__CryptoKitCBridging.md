# `/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 116,896 bytes.

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
@24@0:8^{__SecAccessControl=}16
^{ccss_shamir_share=^{cczp}I[0Q]}16@0:8
Q
@32@0:8@16^{ccec_cp=QQ^{cczp_funcs}[1Q]}24
@44@0:8@16^{ccec_cp=QQ^{cczp_funcs}[1Q]}24B32^i36
@32@0:8@16^i24
^{ccec_cp=QQ^{cczp_funcs}[1Q]}
^{ccec_affine_point=[1Q]}
@36@0:8^{ccss_shamir_parameters=I{cczp=QQ^{cczp_funcs}[1Q]}}16I24@28
I16@0:8
Q24@0:8^{ccec_cp=QQ^{cczp_funcs}[1Q]}16
^{ccec_cp=QQ^{cczp_funcs}[1Q]}16@0:8
r^Q16@0:8
r^Q
@32@0:8^{ccec_affine_point=[1Q]}16^{ccec_cp=QQ^{cczp_funcs}[1Q]}24
^{ccec_affine_point=[1Q]}16@0:8
v16@0:8
@24@0:8^{ccec_cp=QQ^{cczp_funcs}[1Q]}16
B24@0:8@16
@32@0:8^{ccss_shamir_parameters=I{cczp=QQ^{cczp_funcs}[1Q]}}16^{ccss_shamir_share=^{cczp}I[0Q]}24
@16@0:8
^{ccss_shamir_share=^{cczp}I[0Q]}
@32@0:8^Q16^{ccec_cp=QQ^{cczp_funcs}[1Q]}24
@24@0:8^{ccec_pub_ctx=^{ccec_cp}[0{ccec_projective_point=[1Q]}]}16
@20@0:8B16
Failed on import with share import
CKCBCorecryptoECPoint
SEPUtils
CKSSShare
CKCBCorecryptoECScalar
dataFromACL:
initPoint:onGroup:
initWithParams:share:
pointAllocationSizeForGroup:
initWithParams:x:y:
initWithx963Representation:group:
isEqual:
multiply:corecryptoError:
mutableBytes
scalarAllocationSizeForGroup:
corecryptoScalar
share
sub:corecryptoError:
dataWithLength:
y
initWithScalarPointer:forGroup:
_point
group
init
initWithGeneratorForCP:
length
Tr^Q,R,N,V_corecryptoScalar
_group
_share
_share_size
add:corecryptoError:
mapToCurve_SSWU_RandomOracle
serializedPublicKey:
x963Representation
T^{ccec_cp=QQ^{cczp_funcs}[1Q]},R,N,V_group
_corecryptoScalar
inverseModOrder
groupOrderByteCountForCP:
point
T^{ccec_affine_point=[1Q]},R,N,V_point
bytes
initFromPublicKeyBytes:inGroup:compressed:corecryptoError:
initWithPublicKey:
serializedBigEndianScalar
initWithLength:
x
compressedx962PointByteCountForCurveParameters:
initWithData:inGroup:reduction:corecryptoError:
initWithRandomScalarInGroup:
_newZeroingDataWithBytes:length:
dealloc
```
