# `AGXG19FamilyDepthStencilState`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLDepthStencilState`
- 1 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
{DepthStencilState="desc"{DepthStencilStateDescriptorGen2=""(?=""{?="frontFaceStencilCompareFunction"b3"frontFaceStencilFailOperation"b3"frontFaceStencilPassDepthFailOperation"b3"frontFaceStencilPassDepthPassOperation"b3"frontFaceStencilEnabled"b1"backFaceStencilCompareFunction"b3"backFaceStencilFailOperation"b3"backFaceStencilPassDepthFailOperation"b3"backFaceStencilPassDepthPassOperation"b3"backFaceStencilEnabled"b1"depthCompareFunc"b3"depthWriteEnabled"b1"pad"b2"frontface_stencil_read_mask"C"frontface_stencil_write_mask"C"backface_stencil_read_mask"C"backface_stencil_write_mask"C}"dword"Q)"label"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"load_store_needs"S"dss_info"S}"depthstencil_isp_bits"{DepthStencilISPBits="ctl"(_AgxPppStateFrgCommonCtl="all"I"bytes"[4C]"bits"{?="FrontFaceDir"b1"Cullmode"b2"RSVD0"b4"InBatchWindow"b1"TagsortFlushCtl"b2"MrcDependency"b2"RSVD1"b1"TagsortAccumDisable"b1"Visbool"b1"Vistest"b1"Scenable"b1"Dbenable"b1"FaceStencilPres"b1"TwoSided"b1"RectWarpDisable"b1"Tagwritedisable"b1"TwoPassFbOpa"b1"MidRenderCompute"b1"Dboenable"b1"SampleMaskSelect"b1"TriMergeDisable"b1"OverlapCheckMode"b1"UscEsl2"b1"Passtype"b3})"ispa"(_AgxPppStateFrgFaceCtl="all"I"bytes"[4C]"bits"{?="Sref"b8"Pointlinewidth"b10"FillModeOverride"b2"Linefilllastpixel"b1"Dwritedisable"b1"FsDepthDirQual"b2"Dcmpmode"b3"RSVD0"b1"Objtype"b4})}"stencil_isp_bits"{StencilISPBits="fb"(_AgxPppStateFrgFaceStencil="all"I"bytes"[4C]"bits"{?="Swmask"b8"Scmpmask"b8"Sop3"b3"Sop2"b3"Sop1"b3"Scmpmode"b3"RSVD0"b4})"bb"(_AgxPppStateFrgFaceStencil="all"I"bytes"[4C]"bits"{?="Swmask"b8"Scmpmask"b8"Sop3"b3"Sop2"b3"Sop1"b3"Scmpmode"b3"RSVD0"b4})}} _impl;
```

## Properties

```
@property (TB,R) readsDepth;
@property (TB,R) writesDepth;
@property (TB,R) readsStencil;
@property (TB,R) writesStencil;
@property (TQ,R) uniqueIdentifier;
@property (T{MTLResourceID=Q},R) gpuResourceID;
```

## Instance methods

```
-[AGXG19FamilyDepthStencilState uniqueIdentifier];
-[AGXG19FamilyDepthStencilState gpuResourceID];
-[AGXG19FamilyDepthStencilState readsDepth];
-[AGXG19FamilyDepthStencilState readsStencil];
-[AGXG19FamilyDepthStencilState writesDepth];
-[AGXG19FamilyDepthStencilState writesStencil];
```
