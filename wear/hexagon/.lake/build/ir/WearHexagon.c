// Lean compiler output
// Module: WearHexagon
// Imports: public import Init public meta import Init public import Plausible
#include <lean/lean.h>
#if defined(__clang__)
#pragma clang diagnostic ignored "-Wunused-parameter"
#pragma clang diagnostic ignored "-Wunused-label"
#elif defined(__GNUC__) && !defined(__CLANG__)
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-label"
#pragma GCC diagnostic ignored "-Wunused-but-set-variable"
#endif
#ifdef __cplusplus
extern "C" {
#endif
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* l_Repr_addAppParen(lean_object*, lean_object*);
uint8_t lean_nat_dec_le(lean_object*, lean_object*);
lean_object* lean_nat_to_int(lean_object*);
uint8_t lean_nat_dec_le(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ctorIdx(uint8_t);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ctorIdx___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_toCtorIdx(uint8_t);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_toCtorIdx___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ctorElim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ctorElim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ctorElim(lean_object*, lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ctorElim___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_null_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_null_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_null_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_null_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_jogging_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_jogging_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_jogging_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_jogging_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingRotatingArms_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingRotatingArms_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingRotatingArms_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingRotatingArms_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSkipping_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSkipping_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSkipping_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSkipping_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSidesteps_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSidesteps_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSidesteps_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSidesteps_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingButtKicks_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingButtKicks_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingButtKicks_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingButtKicks_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingTriceps_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingTriceps_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingTriceps_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingTriceps_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLunging_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLunging_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLunging_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLunging_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingShoulders_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingShoulders_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingShoulders_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingShoulders_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingHamstrings_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingHamstrings_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingHamstrings_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingHamstrings_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLumbarRotation_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLumbarRotation_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLumbarRotation_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLumbarRotation_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUps_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUps_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUps_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUps_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUpsComplex_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUpsComplex_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUpsComplex_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUpsComplex_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUps_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUps_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUps_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUps_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUpsComplex_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUpsComplex_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUpsComplex_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUpsComplex_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_burpees_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_burpees_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_burpees_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_burpees_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lunges_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lunges_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lunges_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lunges_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lungesComplex_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lungesComplex_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lungesComplex_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lungesComplex_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_benchDips_elim___redArg(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_benchDips_elim___redArg___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_benchDips_elim(lean_object*, uint8_t, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_benchDips_elim___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_WearHexagon_WearHexagon_Activity_ofNat(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ofNat___boxed(lean_object*);
LEAN_EXPORT uint8_t lp_WearHexagon_WearHexagon_instDecidableEqActivity(uint8_t, uint8_t);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_instDecidableEqActivity___boxed(lean_object*, lean_object*);
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 26, .m_capacity = 26, .m_length = 25, .m_data = "WearHexagon.Activity.null"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__0 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__0_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__0_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__1 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__1_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 29, .m_capacity = 29, .m_length = 28, .m_data = "WearHexagon.Activity.jogging"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__2 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__2_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__2_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__3 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__3_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 41, .m_capacity = 41, .m_length = 40, .m_data = "WearHexagon.Activity.joggingRotatingArms"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__4 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__4_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__4_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__5 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__5_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 37, .m_capacity = 37, .m_length = 36, .m_data = "WearHexagon.Activity.joggingSkipping"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__6 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__6_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__6_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__7 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__7_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 38, .m_capacity = 38, .m_length = 37, .m_data = "WearHexagon.Activity.joggingSidesteps"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__8 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__8_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__9_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__8_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__9 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__9_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__10_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 38, .m_capacity = 38, .m_length = 37, .m_data = "WearHexagon.Activity.joggingButtKicks"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__10 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__10_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__11_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__10_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__11 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__11_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__12_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 39, .m_capacity = 39, .m_length = 38, .m_data = "WearHexagon.Activity.stretchingTriceps"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__12 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__12_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__13_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__12_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__13 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__13_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__14_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 39, .m_capacity = 39, .m_length = 38, .m_data = "WearHexagon.Activity.stretchingLunging"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__14 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__14_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__15_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__14_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__15 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__15_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__16_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 41, .m_capacity = 41, .m_length = 40, .m_data = "WearHexagon.Activity.stretchingShoulders"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__16 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__16_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__17_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__16_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__17 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__17_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__18_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 42, .m_capacity = 42, .m_length = 41, .m_data = "WearHexagon.Activity.stretchingHamstrings"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__18 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__18_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__19_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__18_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__19 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__19_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__20_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 46, .m_capacity = 46, .m_length = 45, .m_data = "WearHexagon.Activity.stretchingLumbarRotation"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__20 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__20_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__21_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__20_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__21 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__21_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__22_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 29, .m_capacity = 29, .m_length = 28, .m_data = "WearHexagon.Activity.pushUps"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__22 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__22_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__23_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__22_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__23 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__23_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__24_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 36, .m_capacity = 36, .m_length = 35, .m_data = "WearHexagon.Activity.pushUpsComplex"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__24 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__24_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__25_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__24_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__25 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__25_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__26_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 28, .m_capacity = 28, .m_length = 27, .m_data = "WearHexagon.Activity.sitUps"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__26 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__26_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__27_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__26_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__27 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__27_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__28_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 35, .m_capacity = 35, .m_length = 34, .m_data = "WearHexagon.Activity.sitUpsComplex"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__28 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__28_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__29_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__28_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__29 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__29_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__30_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 29, .m_capacity = 29, .m_length = 28, .m_data = "WearHexagon.Activity.burpees"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__30 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__30_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__31_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__30_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__31 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__31_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__32_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 28, .m_capacity = 28, .m_length = 27, .m_data = "WearHexagon.Activity.lunges"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__32 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__32_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__33_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__32_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__33 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__33_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__34_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 35, .m_capacity = 35, .m_length = 34, .m_data = "WearHexagon.Activity.lungesComplex"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__34 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__34_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__35_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__34_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__35 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__35_value;
static const lean_string_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__36_value = {.m_header = {.m_rc = 0, .m_cs_sz = 0, .m_other = 0, .m_tag = 249}, .m_size = 31, .m_capacity = 31, .m_length = 30, .m_data = "WearHexagon.Activity.benchDips"};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__36 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__36_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__37_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 3}, .m_objs = {((lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__36_value)}};
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__37 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__37_value;
static lean_once_cell_t lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38;
static lean_once_cell_t lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39;
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr(uint8_t, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___boxed(lean_object*, lean_object*);
static const lean_closure_object lp_WearHexagon_WearHexagon_instReprActivity___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_closure_object) + sizeof(void*)*0, .m_other = 0, .m_tag = 245}, .m_fun = (void*)lp_WearHexagon_WearHexagon_instReprActivity_repr___boxed, .m_arity = 2, .m_num_fixed = 0, .m_objs = {} };
static const lean_object* lp_WearHexagon_WearHexagon_instReprActivity___closed__0 = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity___closed__0_value;
LEAN_EXPORT const lean_object* lp_WearHexagon_WearHexagon_instReprActivity = (const lean_object*)&lp_WearHexagon_WearHexagon_instReprActivity___closed__0_value;
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_encode(uint8_t);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_encode___boxed(lean_object*);
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__0_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(18) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__0 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__0_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__1_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(17) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__1 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__1_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__2_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(16) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__2 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__2_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__3_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(15) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__3 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__3_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__4_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(14) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__4 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__4_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__5_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(13) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__5 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__5_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__6_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(12) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__6 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__6_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__7_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(11) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__7 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__7_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__8_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(10) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__8 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__8_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__9_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(9) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__9 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__9_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__10_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(8) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__10 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__10_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__11_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(7) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__11 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__11_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__12_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(6) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__12 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__12_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__13_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(5) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__13 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__13_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__14_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(4) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__14 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__14_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__15_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(3) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__15 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__15_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__16_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(2) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__16 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__16_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__17_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(1) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__17 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__17_value;
static const lean_ctor_object lp_WearHexagon_WearHexagon_decode___closed__18_value = {.m_header = {.m_rc = 0, .m_cs_sz = sizeof(lean_ctor_object) + sizeof(void*)*1 + 0, .m_other = 1, .m_tag = 1}, .m_objs = {((lean_object*)(((size_t)(0) << 1) | 1))}};
static const lean_object* lp_WearHexagon_WearHexagon_decode___closed__18 = (const lean_object*)&lp_WearHexagon_WearHexagon_decode___closed__18_value;
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_decode(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_decode___boxed(lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon___private_WearHexagon_0__WearHexagon_instReprActivity_repr_match__1_splitter___redArg(uint8_t, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon___private_WearHexagon_0__WearHexagon_instReprActivity_repr_match__1_splitter___redArg___boxed(lean_object**);
LEAN_EXPORT lean_object* lp_WearHexagon___private_WearHexagon_0__WearHexagon_instReprActivity_repr_match__1_splitter(lean_object*, uint8_t, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_WearHexagon___private_WearHexagon_0__WearHexagon_instReprActivity_repr_match__1_splitter___boxed(lean_object**);
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ctorIdx(uint8_t v_x_1_){
_start:
{
switch(v_x_1_)
{
case 0:
{
lean_object* v___x_2_; 
v___x_2_ = lean_unsigned_to_nat(0u);
return v___x_2_;
}
case 1:
{
lean_object* v___x_3_; 
v___x_3_ = lean_unsigned_to_nat(1u);
return v___x_3_;
}
case 2:
{
lean_object* v___x_4_; 
v___x_4_ = lean_unsigned_to_nat(2u);
return v___x_4_;
}
case 3:
{
lean_object* v___x_5_; 
v___x_5_ = lean_unsigned_to_nat(3u);
return v___x_5_;
}
case 4:
{
lean_object* v___x_6_; 
v___x_6_ = lean_unsigned_to_nat(4u);
return v___x_6_;
}
case 5:
{
lean_object* v___x_7_; 
v___x_7_ = lean_unsigned_to_nat(5u);
return v___x_7_;
}
case 6:
{
lean_object* v___x_8_; 
v___x_8_ = lean_unsigned_to_nat(6u);
return v___x_8_;
}
case 7:
{
lean_object* v___x_9_; 
v___x_9_ = lean_unsigned_to_nat(7u);
return v___x_9_;
}
case 8:
{
lean_object* v___x_10_; 
v___x_10_ = lean_unsigned_to_nat(8u);
return v___x_10_;
}
case 9:
{
lean_object* v___x_11_; 
v___x_11_ = lean_unsigned_to_nat(9u);
return v___x_11_;
}
case 10:
{
lean_object* v___x_12_; 
v___x_12_ = lean_unsigned_to_nat(10u);
return v___x_12_;
}
case 11:
{
lean_object* v___x_13_; 
v___x_13_ = lean_unsigned_to_nat(11u);
return v___x_13_;
}
case 12:
{
lean_object* v___x_14_; 
v___x_14_ = lean_unsigned_to_nat(12u);
return v___x_14_;
}
case 13:
{
lean_object* v___x_15_; 
v___x_15_ = lean_unsigned_to_nat(13u);
return v___x_15_;
}
case 14:
{
lean_object* v___x_16_; 
v___x_16_ = lean_unsigned_to_nat(14u);
return v___x_16_;
}
case 15:
{
lean_object* v___x_17_; 
v___x_17_ = lean_unsigned_to_nat(15u);
return v___x_17_;
}
case 16:
{
lean_object* v___x_18_; 
v___x_18_ = lean_unsigned_to_nat(16u);
return v___x_18_;
}
case 17:
{
lean_object* v___x_19_; 
v___x_19_ = lean_unsigned_to_nat(17u);
return v___x_19_;
}
default: 
{
lean_object* v___x_20_; 
v___x_20_ = lean_unsigned_to_nat(18u);
return v___x_20_;
}
}
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ctorIdx___boxed(lean_object* v_x_21_){
_start:
{
uint8_t v_x_boxed_22_; lean_object* v_res_23_; 
v_x_boxed_22_ = lean_unbox(v_x_21_);
v_res_23_ = lp_WearHexagon_WearHexagon_Activity_ctorIdx(v_x_boxed_22_);
return v_res_23_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_toCtorIdx(uint8_t v_x_24_){
_start:
{
lean_object* v___x_25_; 
v___x_25_ = lp_WearHexagon_WearHexagon_Activity_ctorIdx(v_x_24_);
return v___x_25_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_toCtorIdx___boxed(lean_object* v_x_26_){
_start:
{
uint8_t v_x_4__boxed_27_; lean_object* v_res_28_; 
v_x_4__boxed_27_ = lean_unbox(v_x_26_);
v_res_28_ = lp_WearHexagon_WearHexagon_Activity_toCtorIdx(v_x_4__boxed_27_);
return v_res_28_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ctorElim___redArg(lean_object* v_k_29_){
_start:
{
lean_inc(v_k_29_);
return v_k_29_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ctorElim___redArg___boxed(lean_object* v_k_30_){
_start:
{
lean_object* v_res_31_; 
v_res_31_ = lp_WearHexagon_WearHexagon_Activity_ctorElim___redArg(v_k_30_);
lean_dec(v_k_30_);
return v_res_31_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ctorElim(lean_object* v_motive_32_, lean_object* v_ctorIdx_33_, uint8_t v_t_34_, lean_object* v_h_35_, lean_object* v_k_36_){
_start:
{
lean_inc(v_k_36_);
return v_k_36_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ctorElim___boxed(lean_object* v_motive_37_, lean_object* v_ctorIdx_38_, lean_object* v_t_39_, lean_object* v_h_40_, lean_object* v_k_41_){
_start:
{
uint8_t v_t_boxed_42_; lean_object* v_res_43_; 
v_t_boxed_42_ = lean_unbox(v_t_39_);
v_res_43_ = lp_WearHexagon_WearHexagon_Activity_ctorElim(v_motive_37_, v_ctorIdx_38_, v_t_boxed_42_, v_h_40_, v_k_41_);
lean_dec(v_k_41_);
lean_dec(v_ctorIdx_38_);
return v_res_43_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_null_elim___redArg(lean_object* v_null_44_){
_start:
{
lean_inc(v_null_44_);
return v_null_44_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_null_elim___redArg___boxed(lean_object* v_null_45_){
_start:
{
lean_object* v_res_46_; 
v_res_46_ = lp_WearHexagon_WearHexagon_Activity_null_elim___redArg(v_null_45_);
lean_dec(v_null_45_);
return v_res_46_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_null_elim(lean_object* v_motive_47_, uint8_t v_t_48_, lean_object* v_h_49_, lean_object* v_null_50_){
_start:
{
lean_inc(v_null_50_);
return v_null_50_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_null_elim___boxed(lean_object* v_motive_51_, lean_object* v_t_52_, lean_object* v_h_53_, lean_object* v_null_54_){
_start:
{
uint8_t v_t_boxed_55_; lean_object* v_res_56_; 
v_t_boxed_55_ = lean_unbox(v_t_52_);
v_res_56_ = lp_WearHexagon_WearHexagon_Activity_null_elim(v_motive_51_, v_t_boxed_55_, v_h_53_, v_null_54_);
lean_dec(v_null_54_);
return v_res_56_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_jogging_elim___redArg(lean_object* v_jogging_57_){
_start:
{
lean_inc(v_jogging_57_);
return v_jogging_57_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_jogging_elim___redArg___boxed(lean_object* v_jogging_58_){
_start:
{
lean_object* v_res_59_; 
v_res_59_ = lp_WearHexagon_WearHexagon_Activity_jogging_elim___redArg(v_jogging_58_);
lean_dec(v_jogging_58_);
return v_res_59_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_jogging_elim(lean_object* v_motive_60_, uint8_t v_t_61_, lean_object* v_h_62_, lean_object* v_jogging_63_){
_start:
{
lean_inc(v_jogging_63_);
return v_jogging_63_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_jogging_elim___boxed(lean_object* v_motive_64_, lean_object* v_t_65_, lean_object* v_h_66_, lean_object* v_jogging_67_){
_start:
{
uint8_t v_t_boxed_68_; lean_object* v_res_69_; 
v_t_boxed_68_ = lean_unbox(v_t_65_);
v_res_69_ = lp_WearHexagon_WearHexagon_Activity_jogging_elim(v_motive_64_, v_t_boxed_68_, v_h_66_, v_jogging_67_);
lean_dec(v_jogging_67_);
return v_res_69_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingRotatingArms_elim___redArg(lean_object* v_joggingRotatingArms_70_){
_start:
{
lean_inc(v_joggingRotatingArms_70_);
return v_joggingRotatingArms_70_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingRotatingArms_elim___redArg___boxed(lean_object* v_joggingRotatingArms_71_){
_start:
{
lean_object* v_res_72_; 
v_res_72_ = lp_WearHexagon_WearHexagon_Activity_joggingRotatingArms_elim___redArg(v_joggingRotatingArms_71_);
lean_dec(v_joggingRotatingArms_71_);
return v_res_72_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingRotatingArms_elim(lean_object* v_motive_73_, uint8_t v_t_74_, lean_object* v_h_75_, lean_object* v_joggingRotatingArms_76_){
_start:
{
lean_inc(v_joggingRotatingArms_76_);
return v_joggingRotatingArms_76_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingRotatingArms_elim___boxed(lean_object* v_motive_77_, lean_object* v_t_78_, lean_object* v_h_79_, lean_object* v_joggingRotatingArms_80_){
_start:
{
uint8_t v_t_boxed_81_; lean_object* v_res_82_; 
v_t_boxed_81_ = lean_unbox(v_t_78_);
v_res_82_ = lp_WearHexagon_WearHexagon_Activity_joggingRotatingArms_elim(v_motive_77_, v_t_boxed_81_, v_h_79_, v_joggingRotatingArms_80_);
lean_dec(v_joggingRotatingArms_80_);
return v_res_82_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSkipping_elim___redArg(lean_object* v_joggingSkipping_83_){
_start:
{
lean_inc(v_joggingSkipping_83_);
return v_joggingSkipping_83_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSkipping_elim___redArg___boxed(lean_object* v_joggingSkipping_84_){
_start:
{
lean_object* v_res_85_; 
v_res_85_ = lp_WearHexagon_WearHexagon_Activity_joggingSkipping_elim___redArg(v_joggingSkipping_84_);
lean_dec(v_joggingSkipping_84_);
return v_res_85_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSkipping_elim(lean_object* v_motive_86_, uint8_t v_t_87_, lean_object* v_h_88_, lean_object* v_joggingSkipping_89_){
_start:
{
lean_inc(v_joggingSkipping_89_);
return v_joggingSkipping_89_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSkipping_elim___boxed(lean_object* v_motive_90_, lean_object* v_t_91_, lean_object* v_h_92_, lean_object* v_joggingSkipping_93_){
_start:
{
uint8_t v_t_boxed_94_; lean_object* v_res_95_; 
v_t_boxed_94_ = lean_unbox(v_t_91_);
v_res_95_ = lp_WearHexagon_WearHexagon_Activity_joggingSkipping_elim(v_motive_90_, v_t_boxed_94_, v_h_92_, v_joggingSkipping_93_);
lean_dec(v_joggingSkipping_93_);
return v_res_95_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSidesteps_elim___redArg(lean_object* v_joggingSidesteps_96_){
_start:
{
lean_inc(v_joggingSidesteps_96_);
return v_joggingSidesteps_96_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSidesteps_elim___redArg___boxed(lean_object* v_joggingSidesteps_97_){
_start:
{
lean_object* v_res_98_; 
v_res_98_ = lp_WearHexagon_WearHexagon_Activity_joggingSidesteps_elim___redArg(v_joggingSidesteps_97_);
lean_dec(v_joggingSidesteps_97_);
return v_res_98_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSidesteps_elim(lean_object* v_motive_99_, uint8_t v_t_100_, lean_object* v_h_101_, lean_object* v_joggingSidesteps_102_){
_start:
{
lean_inc(v_joggingSidesteps_102_);
return v_joggingSidesteps_102_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingSidesteps_elim___boxed(lean_object* v_motive_103_, lean_object* v_t_104_, lean_object* v_h_105_, lean_object* v_joggingSidesteps_106_){
_start:
{
uint8_t v_t_boxed_107_; lean_object* v_res_108_; 
v_t_boxed_107_ = lean_unbox(v_t_104_);
v_res_108_ = lp_WearHexagon_WearHexagon_Activity_joggingSidesteps_elim(v_motive_103_, v_t_boxed_107_, v_h_105_, v_joggingSidesteps_106_);
lean_dec(v_joggingSidesteps_106_);
return v_res_108_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingButtKicks_elim___redArg(lean_object* v_joggingButtKicks_109_){
_start:
{
lean_inc(v_joggingButtKicks_109_);
return v_joggingButtKicks_109_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingButtKicks_elim___redArg___boxed(lean_object* v_joggingButtKicks_110_){
_start:
{
lean_object* v_res_111_; 
v_res_111_ = lp_WearHexagon_WearHexagon_Activity_joggingButtKicks_elim___redArg(v_joggingButtKicks_110_);
lean_dec(v_joggingButtKicks_110_);
return v_res_111_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingButtKicks_elim(lean_object* v_motive_112_, uint8_t v_t_113_, lean_object* v_h_114_, lean_object* v_joggingButtKicks_115_){
_start:
{
lean_inc(v_joggingButtKicks_115_);
return v_joggingButtKicks_115_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_joggingButtKicks_elim___boxed(lean_object* v_motive_116_, lean_object* v_t_117_, lean_object* v_h_118_, lean_object* v_joggingButtKicks_119_){
_start:
{
uint8_t v_t_boxed_120_; lean_object* v_res_121_; 
v_t_boxed_120_ = lean_unbox(v_t_117_);
v_res_121_ = lp_WearHexagon_WearHexagon_Activity_joggingButtKicks_elim(v_motive_116_, v_t_boxed_120_, v_h_118_, v_joggingButtKicks_119_);
lean_dec(v_joggingButtKicks_119_);
return v_res_121_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingTriceps_elim___redArg(lean_object* v_stretchingTriceps_122_){
_start:
{
lean_inc(v_stretchingTriceps_122_);
return v_stretchingTriceps_122_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingTriceps_elim___redArg___boxed(lean_object* v_stretchingTriceps_123_){
_start:
{
lean_object* v_res_124_; 
v_res_124_ = lp_WearHexagon_WearHexagon_Activity_stretchingTriceps_elim___redArg(v_stretchingTriceps_123_);
lean_dec(v_stretchingTriceps_123_);
return v_res_124_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingTriceps_elim(lean_object* v_motive_125_, uint8_t v_t_126_, lean_object* v_h_127_, lean_object* v_stretchingTriceps_128_){
_start:
{
lean_inc(v_stretchingTriceps_128_);
return v_stretchingTriceps_128_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingTriceps_elim___boxed(lean_object* v_motive_129_, lean_object* v_t_130_, lean_object* v_h_131_, lean_object* v_stretchingTriceps_132_){
_start:
{
uint8_t v_t_boxed_133_; lean_object* v_res_134_; 
v_t_boxed_133_ = lean_unbox(v_t_130_);
v_res_134_ = lp_WearHexagon_WearHexagon_Activity_stretchingTriceps_elim(v_motive_129_, v_t_boxed_133_, v_h_131_, v_stretchingTriceps_132_);
lean_dec(v_stretchingTriceps_132_);
return v_res_134_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLunging_elim___redArg(lean_object* v_stretchingLunging_135_){
_start:
{
lean_inc(v_stretchingLunging_135_);
return v_stretchingLunging_135_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLunging_elim___redArg___boxed(lean_object* v_stretchingLunging_136_){
_start:
{
lean_object* v_res_137_; 
v_res_137_ = lp_WearHexagon_WearHexagon_Activity_stretchingLunging_elim___redArg(v_stretchingLunging_136_);
lean_dec(v_stretchingLunging_136_);
return v_res_137_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLunging_elim(lean_object* v_motive_138_, uint8_t v_t_139_, lean_object* v_h_140_, lean_object* v_stretchingLunging_141_){
_start:
{
lean_inc(v_stretchingLunging_141_);
return v_stretchingLunging_141_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLunging_elim___boxed(lean_object* v_motive_142_, lean_object* v_t_143_, lean_object* v_h_144_, lean_object* v_stretchingLunging_145_){
_start:
{
uint8_t v_t_boxed_146_; lean_object* v_res_147_; 
v_t_boxed_146_ = lean_unbox(v_t_143_);
v_res_147_ = lp_WearHexagon_WearHexagon_Activity_stretchingLunging_elim(v_motive_142_, v_t_boxed_146_, v_h_144_, v_stretchingLunging_145_);
lean_dec(v_stretchingLunging_145_);
return v_res_147_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingShoulders_elim___redArg(lean_object* v_stretchingShoulders_148_){
_start:
{
lean_inc(v_stretchingShoulders_148_);
return v_stretchingShoulders_148_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingShoulders_elim___redArg___boxed(lean_object* v_stretchingShoulders_149_){
_start:
{
lean_object* v_res_150_; 
v_res_150_ = lp_WearHexagon_WearHexagon_Activity_stretchingShoulders_elim___redArg(v_stretchingShoulders_149_);
lean_dec(v_stretchingShoulders_149_);
return v_res_150_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingShoulders_elim(lean_object* v_motive_151_, uint8_t v_t_152_, lean_object* v_h_153_, lean_object* v_stretchingShoulders_154_){
_start:
{
lean_inc(v_stretchingShoulders_154_);
return v_stretchingShoulders_154_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingShoulders_elim___boxed(lean_object* v_motive_155_, lean_object* v_t_156_, lean_object* v_h_157_, lean_object* v_stretchingShoulders_158_){
_start:
{
uint8_t v_t_boxed_159_; lean_object* v_res_160_; 
v_t_boxed_159_ = lean_unbox(v_t_156_);
v_res_160_ = lp_WearHexagon_WearHexagon_Activity_stretchingShoulders_elim(v_motive_155_, v_t_boxed_159_, v_h_157_, v_stretchingShoulders_158_);
lean_dec(v_stretchingShoulders_158_);
return v_res_160_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingHamstrings_elim___redArg(lean_object* v_stretchingHamstrings_161_){
_start:
{
lean_inc(v_stretchingHamstrings_161_);
return v_stretchingHamstrings_161_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingHamstrings_elim___redArg___boxed(lean_object* v_stretchingHamstrings_162_){
_start:
{
lean_object* v_res_163_; 
v_res_163_ = lp_WearHexagon_WearHexagon_Activity_stretchingHamstrings_elim___redArg(v_stretchingHamstrings_162_);
lean_dec(v_stretchingHamstrings_162_);
return v_res_163_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingHamstrings_elim(lean_object* v_motive_164_, uint8_t v_t_165_, lean_object* v_h_166_, lean_object* v_stretchingHamstrings_167_){
_start:
{
lean_inc(v_stretchingHamstrings_167_);
return v_stretchingHamstrings_167_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingHamstrings_elim___boxed(lean_object* v_motive_168_, lean_object* v_t_169_, lean_object* v_h_170_, lean_object* v_stretchingHamstrings_171_){
_start:
{
uint8_t v_t_boxed_172_; lean_object* v_res_173_; 
v_t_boxed_172_ = lean_unbox(v_t_169_);
v_res_173_ = lp_WearHexagon_WearHexagon_Activity_stretchingHamstrings_elim(v_motive_168_, v_t_boxed_172_, v_h_170_, v_stretchingHamstrings_171_);
lean_dec(v_stretchingHamstrings_171_);
return v_res_173_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLumbarRotation_elim___redArg(lean_object* v_stretchingLumbarRotation_174_){
_start:
{
lean_inc(v_stretchingLumbarRotation_174_);
return v_stretchingLumbarRotation_174_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLumbarRotation_elim___redArg___boxed(lean_object* v_stretchingLumbarRotation_175_){
_start:
{
lean_object* v_res_176_; 
v_res_176_ = lp_WearHexagon_WearHexagon_Activity_stretchingLumbarRotation_elim___redArg(v_stretchingLumbarRotation_175_);
lean_dec(v_stretchingLumbarRotation_175_);
return v_res_176_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLumbarRotation_elim(lean_object* v_motive_177_, uint8_t v_t_178_, lean_object* v_h_179_, lean_object* v_stretchingLumbarRotation_180_){
_start:
{
lean_inc(v_stretchingLumbarRotation_180_);
return v_stretchingLumbarRotation_180_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_stretchingLumbarRotation_elim___boxed(lean_object* v_motive_181_, lean_object* v_t_182_, lean_object* v_h_183_, lean_object* v_stretchingLumbarRotation_184_){
_start:
{
uint8_t v_t_boxed_185_; lean_object* v_res_186_; 
v_t_boxed_185_ = lean_unbox(v_t_182_);
v_res_186_ = lp_WearHexagon_WearHexagon_Activity_stretchingLumbarRotation_elim(v_motive_181_, v_t_boxed_185_, v_h_183_, v_stretchingLumbarRotation_184_);
lean_dec(v_stretchingLumbarRotation_184_);
return v_res_186_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUps_elim___redArg(lean_object* v_pushUps_187_){
_start:
{
lean_inc(v_pushUps_187_);
return v_pushUps_187_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUps_elim___redArg___boxed(lean_object* v_pushUps_188_){
_start:
{
lean_object* v_res_189_; 
v_res_189_ = lp_WearHexagon_WearHexagon_Activity_pushUps_elim___redArg(v_pushUps_188_);
lean_dec(v_pushUps_188_);
return v_res_189_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUps_elim(lean_object* v_motive_190_, uint8_t v_t_191_, lean_object* v_h_192_, lean_object* v_pushUps_193_){
_start:
{
lean_inc(v_pushUps_193_);
return v_pushUps_193_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUps_elim___boxed(lean_object* v_motive_194_, lean_object* v_t_195_, lean_object* v_h_196_, lean_object* v_pushUps_197_){
_start:
{
uint8_t v_t_boxed_198_; lean_object* v_res_199_; 
v_t_boxed_198_ = lean_unbox(v_t_195_);
v_res_199_ = lp_WearHexagon_WearHexagon_Activity_pushUps_elim(v_motive_194_, v_t_boxed_198_, v_h_196_, v_pushUps_197_);
lean_dec(v_pushUps_197_);
return v_res_199_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUpsComplex_elim___redArg(lean_object* v_pushUpsComplex_200_){
_start:
{
lean_inc(v_pushUpsComplex_200_);
return v_pushUpsComplex_200_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUpsComplex_elim___redArg___boxed(lean_object* v_pushUpsComplex_201_){
_start:
{
lean_object* v_res_202_; 
v_res_202_ = lp_WearHexagon_WearHexagon_Activity_pushUpsComplex_elim___redArg(v_pushUpsComplex_201_);
lean_dec(v_pushUpsComplex_201_);
return v_res_202_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUpsComplex_elim(lean_object* v_motive_203_, uint8_t v_t_204_, lean_object* v_h_205_, lean_object* v_pushUpsComplex_206_){
_start:
{
lean_inc(v_pushUpsComplex_206_);
return v_pushUpsComplex_206_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_pushUpsComplex_elim___boxed(lean_object* v_motive_207_, lean_object* v_t_208_, lean_object* v_h_209_, lean_object* v_pushUpsComplex_210_){
_start:
{
uint8_t v_t_boxed_211_; lean_object* v_res_212_; 
v_t_boxed_211_ = lean_unbox(v_t_208_);
v_res_212_ = lp_WearHexagon_WearHexagon_Activity_pushUpsComplex_elim(v_motive_207_, v_t_boxed_211_, v_h_209_, v_pushUpsComplex_210_);
lean_dec(v_pushUpsComplex_210_);
return v_res_212_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUps_elim___redArg(lean_object* v_sitUps_213_){
_start:
{
lean_inc(v_sitUps_213_);
return v_sitUps_213_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUps_elim___redArg___boxed(lean_object* v_sitUps_214_){
_start:
{
lean_object* v_res_215_; 
v_res_215_ = lp_WearHexagon_WearHexagon_Activity_sitUps_elim___redArg(v_sitUps_214_);
lean_dec(v_sitUps_214_);
return v_res_215_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUps_elim(lean_object* v_motive_216_, uint8_t v_t_217_, lean_object* v_h_218_, lean_object* v_sitUps_219_){
_start:
{
lean_inc(v_sitUps_219_);
return v_sitUps_219_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUps_elim___boxed(lean_object* v_motive_220_, lean_object* v_t_221_, lean_object* v_h_222_, lean_object* v_sitUps_223_){
_start:
{
uint8_t v_t_boxed_224_; lean_object* v_res_225_; 
v_t_boxed_224_ = lean_unbox(v_t_221_);
v_res_225_ = lp_WearHexagon_WearHexagon_Activity_sitUps_elim(v_motive_220_, v_t_boxed_224_, v_h_222_, v_sitUps_223_);
lean_dec(v_sitUps_223_);
return v_res_225_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUpsComplex_elim___redArg(lean_object* v_sitUpsComplex_226_){
_start:
{
lean_inc(v_sitUpsComplex_226_);
return v_sitUpsComplex_226_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUpsComplex_elim___redArg___boxed(lean_object* v_sitUpsComplex_227_){
_start:
{
lean_object* v_res_228_; 
v_res_228_ = lp_WearHexagon_WearHexagon_Activity_sitUpsComplex_elim___redArg(v_sitUpsComplex_227_);
lean_dec(v_sitUpsComplex_227_);
return v_res_228_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUpsComplex_elim(lean_object* v_motive_229_, uint8_t v_t_230_, lean_object* v_h_231_, lean_object* v_sitUpsComplex_232_){
_start:
{
lean_inc(v_sitUpsComplex_232_);
return v_sitUpsComplex_232_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_sitUpsComplex_elim___boxed(lean_object* v_motive_233_, lean_object* v_t_234_, lean_object* v_h_235_, lean_object* v_sitUpsComplex_236_){
_start:
{
uint8_t v_t_boxed_237_; lean_object* v_res_238_; 
v_t_boxed_237_ = lean_unbox(v_t_234_);
v_res_238_ = lp_WearHexagon_WearHexagon_Activity_sitUpsComplex_elim(v_motive_233_, v_t_boxed_237_, v_h_235_, v_sitUpsComplex_236_);
lean_dec(v_sitUpsComplex_236_);
return v_res_238_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_burpees_elim___redArg(lean_object* v_burpees_239_){
_start:
{
lean_inc(v_burpees_239_);
return v_burpees_239_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_burpees_elim___redArg___boxed(lean_object* v_burpees_240_){
_start:
{
lean_object* v_res_241_; 
v_res_241_ = lp_WearHexagon_WearHexagon_Activity_burpees_elim___redArg(v_burpees_240_);
lean_dec(v_burpees_240_);
return v_res_241_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_burpees_elim(lean_object* v_motive_242_, uint8_t v_t_243_, lean_object* v_h_244_, lean_object* v_burpees_245_){
_start:
{
lean_inc(v_burpees_245_);
return v_burpees_245_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_burpees_elim___boxed(lean_object* v_motive_246_, lean_object* v_t_247_, lean_object* v_h_248_, lean_object* v_burpees_249_){
_start:
{
uint8_t v_t_boxed_250_; lean_object* v_res_251_; 
v_t_boxed_250_ = lean_unbox(v_t_247_);
v_res_251_ = lp_WearHexagon_WearHexagon_Activity_burpees_elim(v_motive_246_, v_t_boxed_250_, v_h_248_, v_burpees_249_);
lean_dec(v_burpees_249_);
return v_res_251_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lunges_elim___redArg(lean_object* v_lunges_252_){
_start:
{
lean_inc(v_lunges_252_);
return v_lunges_252_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lunges_elim___redArg___boxed(lean_object* v_lunges_253_){
_start:
{
lean_object* v_res_254_; 
v_res_254_ = lp_WearHexagon_WearHexagon_Activity_lunges_elim___redArg(v_lunges_253_);
lean_dec(v_lunges_253_);
return v_res_254_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lunges_elim(lean_object* v_motive_255_, uint8_t v_t_256_, lean_object* v_h_257_, lean_object* v_lunges_258_){
_start:
{
lean_inc(v_lunges_258_);
return v_lunges_258_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lunges_elim___boxed(lean_object* v_motive_259_, lean_object* v_t_260_, lean_object* v_h_261_, lean_object* v_lunges_262_){
_start:
{
uint8_t v_t_boxed_263_; lean_object* v_res_264_; 
v_t_boxed_263_ = lean_unbox(v_t_260_);
v_res_264_ = lp_WearHexagon_WearHexagon_Activity_lunges_elim(v_motive_259_, v_t_boxed_263_, v_h_261_, v_lunges_262_);
lean_dec(v_lunges_262_);
return v_res_264_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lungesComplex_elim___redArg(lean_object* v_lungesComplex_265_){
_start:
{
lean_inc(v_lungesComplex_265_);
return v_lungesComplex_265_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lungesComplex_elim___redArg___boxed(lean_object* v_lungesComplex_266_){
_start:
{
lean_object* v_res_267_; 
v_res_267_ = lp_WearHexagon_WearHexagon_Activity_lungesComplex_elim___redArg(v_lungesComplex_266_);
lean_dec(v_lungesComplex_266_);
return v_res_267_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lungesComplex_elim(lean_object* v_motive_268_, uint8_t v_t_269_, lean_object* v_h_270_, lean_object* v_lungesComplex_271_){
_start:
{
lean_inc(v_lungesComplex_271_);
return v_lungesComplex_271_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_lungesComplex_elim___boxed(lean_object* v_motive_272_, lean_object* v_t_273_, lean_object* v_h_274_, lean_object* v_lungesComplex_275_){
_start:
{
uint8_t v_t_boxed_276_; lean_object* v_res_277_; 
v_t_boxed_276_ = lean_unbox(v_t_273_);
v_res_277_ = lp_WearHexagon_WearHexagon_Activity_lungesComplex_elim(v_motive_272_, v_t_boxed_276_, v_h_274_, v_lungesComplex_275_);
lean_dec(v_lungesComplex_275_);
return v_res_277_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_benchDips_elim___redArg(lean_object* v_benchDips_278_){
_start:
{
lean_inc(v_benchDips_278_);
return v_benchDips_278_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_benchDips_elim___redArg___boxed(lean_object* v_benchDips_279_){
_start:
{
lean_object* v_res_280_; 
v_res_280_ = lp_WearHexagon_WearHexagon_Activity_benchDips_elim___redArg(v_benchDips_279_);
lean_dec(v_benchDips_279_);
return v_res_280_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_benchDips_elim(lean_object* v_motive_281_, uint8_t v_t_282_, lean_object* v_h_283_, lean_object* v_benchDips_284_){
_start:
{
lean_inc(v_benchDips_284_);
return v_benchDips_284_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_benchDips_elim___boxed(lean_object* v_motive_285_, lean_object* v_t_286_, lean_object* v_h_287_, lean_object* v_benchDips_288_){
_start:
{
uint8_t v_t_boxed_289_; lean_object* v_res_290_; 
v_t_boxed_289_ = lean_unbox(v_t_286_);
v_res_290_ = lp_WearHexagon_WearHexagon_Activity_benchDips_elim(v_motive_285_, v_t_boxed_289_, v_h_287_, v_benchDips_288_);
lean_dec(v_benchDips_288_);
return v_res_290_;
}
}
LEAN_EXPORT uint8_t lp_WearHexagon_WearHexagon_Activity_ofNat(lean_object* v_n_291_){
_start:
{
lean_object* v___x_292_; uint8_t v___x_293_; 
v___x_292_ = lean_unsigned_to_nat(8u);
v___x_293_ = lean_nat_dec_le(v_n_291_, v___x_292_);
if (v___x_293_ == 0)
{
lean_object* v___x_294_; uint8_t v___x_295_; 
v___x_294_ = lean_unsigned_to_nat(13u);
v___x_295_ = lean_nat_dec_le(v_n_291_, v___x_294_);
if (v___x_295_ == 0)
{
lean_object* v___x_296_; uint8_t v___x_297_; 
v___x_296_ = lean_unsigned_to_nat(15u);
v___x_297_ = lean_nat_dec_le(v_n_291_, v___x_296_);
if (v___x_297_ == 0)
{
lean_object* v___x_298_; uint8_t v___x_299_; 
v___x_298_ = lean_unsigned_to_nat(16u);
v___x_299_ = lean_nat_dec_le(v_n_291_, v___x_298_);
if (v___x_299_ == 0)
{
lean_object* v___x_300_; uint8_t v___x_301_; 
v___x_300_ = lean_unsigned_to_nat(17u);
v___x_301_ = lean_nat_dec_le(v_n_291_, v___x_300_);
if (v___x_301_ == 0)
{
uint8_t v___x_302_; 
v___x_302_ = 18;
return v___x_302_;
}
else
{
uint8_t v___x_303_; 
v___x_303_ = 17;
return v___x_303_;
}
}
else
{
uint8_t v___x_304_; 
v___x_304_ = 16;
return v___x_304_;
}
}
else
{
lean_object* v___x_305_; uint8_t v___x_306_; 
v___x_305_ = lean_unsigned_to_nat(14u);
v___x_306_ = lean_nat_dec_le(v_n_291_, v___x_305_);
if (v___x_306_ == 0)
{
uint8_t v___x_307_; 
v___x_307_ = 15;
return v___x_307_;
}
else
{
uint8_t v___x_308_; 
v___x_308_ = 14;
return v___x_308_;
}
}
}
else
{
lean_object* v___x_309_; uint8_t v___x_310_; 
v___x_309_ = lean_unsigned_to_nat(10u);
v___x_310_ = lean_nat_dec_le(v_n_291_, v___x_309_);
if (v___x_310_ == 0)
{
lean_object* v___x_311_; uint8_t v___x_312_; 
v___x_311_ = lean_unsigned_to_nat(11u);
v___x_312_ = lean_nat_dec_le(v_n_291_, v___x_311_);
if (v___x_312_ == 0)
{
lean_object* v___x_313_; uint8_t v___x_314_; 
v___x_313_ = lean_unsigned_to_nat(12u);
v___x_314_ = lean_nat_dec_le(v_n_291_, v___x_313_);
if (v___x_314_ == 0)
{
uint8_t v___x_315_; 
v___x_315_ = 13;
return v___x_315_;
}
else
{
uint8_t v___x_316_; 
v___x_316_ = 12;
return v___x_316_;
}
}
else
{
uint8_t v___x_317_; 
v___x_317_ = 11;
return v___x_317_;
}
}
else
{
lean_object* v___x_318_; uint8_t v___x_319_; 
v___x_318_ = lean_unsigned_to_nat(9u);
v___x_319_ = lean_nat_dec_le(v_n_291_, v___x_318_);
if (v___x_319_ == 0)
{
uint8_t v___x_320_; 
v___x_320_ = 10;
return v___x_320_;
}
else
{
uint8_t v___x_321_; 
v___x_321_ = 9;
return v___x_321_;
}
}
}
}
else
{
lean_object* v___x_322_; uint8_t v___x_323_; 
v___x_322_ = lean_unsigned_to_nat(3u);
v___x_323_ = lean_nat_dec_le(v_n_291_, v___x_322_);
if (v___x_323_ == 0)
{
lean_object* v___x_324_; uint8_t v___x_325_; 
v___x_324_ = lean_unsigned_to_nat(5u);
v___x_325_ = lean_nat_dec_le(v_n_291_, v___x_324_);
if (v___x_325_ == 0)
{
lean_object* v___x_326_; uint8_t v___x_327_; 
v___x_326_ = lean_unsigned_to_nat(6u);
v___x_327_ = lean_nat_dec_le(v_n_291_, v___x_326_);
if (v___x_327_ == 0)
{
lean_object* v___x_328_; uint8_t v___x_329_; 
v___x_328_ = lean_unsigned_to_nat(7u);
v___x_329_ = lean_nat_dec_le(v_n_291_, v___x_328_);
if (v___x_329_ == 0)
{
uint8_t v___x_330_; 
v___x_330_ = 8;
return v___x_330_;
}
else
{
uint8_t v___x_331_; 
v___x_331_ = 7;
return v___x_331_;
}
}
else
{
uint8_t v___x_332_; 
v___x_332_ = 6;
return v___x_332_;
}
}
else
{
lean_object* v___x_333_; uint8_t v___x_334_; 
v___x_333_ = lean_unsigned_to_nat(4u);
v___x_334_ = lean_nat_dec_le(v_n_291_, v___x_333_);
if (v___x_334_ == 0)
{
uint8_t v___x_335_; 
v___x_335_ = 5;
return v___x_335_;
}
else
{
uint8_t v___x_336_; 
v___x_336_ = 4;
return v___x_336_;
}
}
}
else
{
lean_object* v___x_337_; uint8_t v___x_338_; 
v___x_337_ = lean_unsigned_to_nat(1u);
v___x_338_ = lean_nat_dec_le(v_n_291_, v___x_337_);
if (v___x_338_ == 0)
{
lean_object* v___x_339_; uint8_t v___x_340_; 
v___x_339_ = lean_unsigned_to_nat(2u);
v___x_340_ = lean_nat_dec_le(v_n_291_, v___x_339_);
if (v___x_340_ == 0)
{
uint8_t v___x_341_; 
v___x_341_ = 3;
return v___x_341_;
}
else
{
uint8_t v___x_342_; 
v___x_342_ = 2;
return v___x_342_;
}
}
else
{
lean_object* v___x_343_; uint8_t v___x_344_; 
v___x_343_ = lean_unsigned_to_nat(0u);
v___x_344_ = lean_nat_dec_le(v_n_291_, v___x_343_);
if (v___x_344_ == 0)
{
uint8_t v___x_345_; 
v___x_345_ = 1;
return v___x_345_;
}
else
{
uint8_t v___x_346_; 
v___x_346_ = 0;
return v___x_346_;
}
}
}
}
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_Activity_ofNat___boxed(lean_object* v_n_347_){
_start:
{
uint8_t v_res_348_; lean_object* v_r_349_; 
v_res_348_ = lp_WearHexagon_WearHexagon_Activity_ofNat(v_n_347_);
lean_dec(v_n_347_);
v_r_349_ = lean_box(v_res_348_);
return v_r_349_;
}
}
LEAN_EXPORT uint8_t lp_WearHexagon_WearHexagon_instDecidableEqActivity(uint8_t v_x_350_, uint8_t v_y_351_){
_start:
{
lean_object* v___x_352_; lean_object* v___x_353_; uint8_t v___x_354_; 
v___x_352_ = lp_WearHexagon_WearHexagon_Activity_ctorIdx(v_x_350_);
v___x_353_ = lp_WearHexagon_WearHexagon_Activity_ctorIdx(v_y_351_);
v___x_354_ = lean_nat_dec_eq(v___x_352_, v___x_353_);
lean_dec(v___x_353_);
lean_dec(v___x_352_);
return v___x_354_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_instDecidableEqActivity___boxed(lean_object* v_x_355_, lean_object* v_y_356_){
_start:
{
uint8_t v_x_13__boxed_357_; uint8_t v_y_14__boxed_358_; uint8_t v_res_359_; lean_object* v_r_360_; 
v_x_13__boxed_357_ = lean_unbox(v_x_355_);
v_y_14__boxed_358_ = lean_unbox(v_y_356_);
v_res_359_ = lp_WearHexagon_WearHexagon_instDecidableEqActivity(v_x_13__boxed_357_, v_y_14__boxed_358_);
v_r_360_ = lean_box(v_res_359_);
return v_r_360_;
}
}
static lean_object* _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38(void){
_start:
{
lean_object* v___x_418_; lean_object* v___x_419_; 
v___x_418_ = lean_unsigned_to_nat(2u);
v___x_419_ = lean_nat_to_int(v___x_418_);
return v___x_419_;
}
}
static lean_object* _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39(void){
_start:
{
lean_object* v___x_420_; lean_object* v___x_421_; 
v___x_420_ = lean_unsigned_to_nat(1u);
v___x_421_ = lean_nat_to_int(v___x_420_);
return v___x_421_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr(uint8_t v_x_422_, lean_object* v_prec_423_){
_start:
{
lean_object* v___y_425_; lean_object* v___y_432_; lean_object* v___y_439_; lean_object* v___y_446_; lean_object* v___y_453_; lean_object* v___y_460_; lean_object* v___y_467_; lean_object* v___y_474_; lean_object* v___y_481_; lean_object* v___y_488_; lean_object* v___y_495_; lean_object* v___y_502_; lean_object* v___y_509_; lean_object* v___y_516_; lean_object* v___y_523_; lean_object* v___y_530_; lean_object* v___y_537_; lean_object* v___y_544_; lean_object* v___y_551_; 
switch(v_x_422_)
{
case 0:
{
lean_object* v___x_557_; uint8_t v___x_558_; 
v___x_557_ = lean_unsigned_to_nat(1024u);
v___x_558_ = lean_nat_dec_le(v___x_557_, v_prec_423_);
if (v___x_558_ == 0)
{
lean_object* v___x_559_; 
v___x_559_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_425_ = v___x_559_;
goto v___jp_424_;
}
else
{
lean_object* v___x_560_; 
v___x_560_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_425_ = v___x_560_;
goto v___jp_424_;
}
}
case 1:
{
lean_object* v___x_561_; uint8_t v___x_562_; 
v___x_561_ = lean_unsigned_to_nat(1024u);
v___x_562_ = lean_nat_dec_le(v___x_561_, v_prec_423_);
if (v___x_562_ == 0)
{
lean_object* v___x_563_; 
v___x_563_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_432_ = v___x_563_;
goto v___jp_431_;
}
else
{
lean_object* v___x_564_; 
v___x_564_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_432_ = v___x_564_;
goto v___jp_431_;
}
}
case 2:
{
lean_object* v___x_565_; uint8_t v___x_566_; 
v___x_565_ = lean_unsigned_to_nat(1024u);
v___x_566_ = lean_nat_dec_le(v___x_565_, v_prec_423_);
if (v___x_566_ == 0)
{
lean_object* v___x_567_; 
v___x_567_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_439_ = v___x_567_;
goto v___jp_438_;
}
else
{
lean_object* v___x_568_; 
v___x_568_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_439_ = v___x_568_;
goto v___jp_438_;
}
}
case 3:
{
lean_object* v___x_569_; uint8_t v___x_570_; 
v___x_569_ = lean_unsigned_to_nat(1024u);
v___x_570_ = lean_nat_dec_le(v___x_569_, v_prec_423_);
if (v___x_570_ == 0)
{
lean_object* v___x_571_; 
v___x_571_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_446_ = v___x_571_;
goto v___jp_445_;
}
else
{
lean_object* v___x_572_; 
v___x_572_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_446_ = v___x_572_;
goto v___jp_445_;
}
}
case 4:
{
lean_object* v___x_573_; uint8_t v___x_574_; 
v___x_573_ = lean_unsigned_to_nat(1024u);
v___x_574_ = lean_nat_dec_le(v___x_573_, v_prec_423_);
if (v___x_574_ == 0)
{
lean_object* v___x_575_; 
v___x_575_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_453_ = v___x_575_;
goto v___jp_452_;
}
else
{
lean_object* v___x_576_; 
v___x_576_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_453_ = v___x_576_;
goto v___jp_452_;
}
}
case 5:
{
lean_object* v___x_577_; uint8_t v___x_578_; 
v___x_577_ = lean_unsigned_to_nat(1024u);
v___x_578_ = lean_nat_dec_le(v___x_577_, v_prec_423_);
if (v___x_578_ == 0)
{
lean_object* v___x_579_; 
v___x_579_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_460_ = v___x_579_;
goto v___jp_459_;
}
else
{
lean_object* v___x_580_; 
v___x_580_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_460_ = v___x_580_;
goto v___jp_459_;
}
}
case 6:
{
lean_object* v___x_581_; uint8_t v___x_582_; 
v___x_581_ = lean_unsigned_to_nat(1024u);
v___x_582_ = lean_nat_dec_le(v___x_581_, v_prec_423_);
if (v___x_582_ == 0)
{
lean_object* v___x_583_; 
v___x_583_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_467_ = v___x_583_;
goto v___jp_466_;
}
else
{
lean_object* v___x_584_; 
v___x_584_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_467_ = v___x_584_;
goto v___jp_466_;
}
}
case 7:
{
lean_object* v___x_585_; uint8_t v___x_586_; 
v___x_585_ = lean_unsigned_to_nat(1024u);
v___x_586_ = lean_nat_dec_le(v___x_585_, v_prec_423_);
if (v___x_586_ == 0)
{
lean_object* v___x_587_; 
v___x_587_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_474_ = v___x_587_;
goto v___jp_473_;
}
else
{
lean_object* v___x_588_; 
v___x_588_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_474_ = v___x_588_;
goto v___jp_473_;
}
}
case 8:
{
lean_object* v___x_589_; uint8_t v___x_590_; 
v___x_589_ = lean_unsigned_to_nat(1024u);
v___x_590_ = lean_nat_dec_le(v___x_589_, v_prec_423_);
if (v___x_590_ == 0)
{
lean_object* v___x_591_; 
v___x_591_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_481_ = v___x_591_;
goto v___jp_480_;
}
else
{
lean_object* v___x_592_; 
v___x_592_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_481_ = v___x_592_;
goto v___jp_480_;
}
}
case 9:
{
lean_object* v___x_593_; uint8_t v___x_594_; 
v___x_593_ = lean_unsigned_to_nat(1024u);
v___x_594_ = lean_nat_dec_le(v___x_593_, v_prec_423_);
if (v___x_594_ == 0)
{
lean_object* v___x_595_; 
v___x_595_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_488_ = v___x_595_;
goto v___jp_487_;
}
else
{
lean_object* v___x_596_; 
v___x_596_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_488_ = v___x_596_;
goto v___jp_487_;
}
}
case 10:
{
lean_object* v___x_597_; uint8_t v___x_598_; 
v___x_597_ = lean_unsigned_to_nat(1024u);
v___x_598_ = lean_nat_dec_le(v___x_597_, v_prec_423_);
if (v___x_598_ == 0)
{
lean_object* v___x_599_; 
v___x_599_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_495_ = v___x_599_;
goto v___jp_494_;
}
else
{
lean_object* v___x_600_; 
v___x_600_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_495_ = v___x_600_;
goto v___jp_494_;
}
}
case 11:
{
lean_object* v___x_601_; uint8_t v___x_602_; 
v___x_601_ = lean_unsigned_to_nat(1024u);
v___x_602_ = lean_nat_dec_le(v___x_601_, v_prec_423_);
if (v___x_602_ == 0)
{
lean_object* v___x_603_; 
v___x_603_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_502_ = v___x_603_;
goto v___jp_501_;
}
else
{
lean_object* v___x_604_; 
v___x_604_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_502_ = v___x_604_;
goto v___jp_501_;
}
}
case 12:
{
lean_object* v___x_605_; uint8_t v___x_606_; 
v___x_605_ = lean_unsigned_to_nat(1024u);
v___x_606_ = lean_nat_dec_le(v___x_605_, v_prec_423_);
if (v___x_606_ == 0)
{
lean_object* v___x_607_; 
v___x_607_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_509_ = v___x_607_;
goto v___jp_508_;
}
else
{
lean_object* v___x_608_; 
v___x_608_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_509_ = v___x_608_;
goto v___jp_508_;
}
}
case 13:
{
lean_object* v___x_609_; uint8_t v___x_610_; 
v___x_609_ = lean_unsigned_to_nat(1024u);
v___x_610_ = lean_nat_dec_le(v___x_609_, v_prec_423_);
if (v___x_610_ == 0)
{
lean_object* v___x_611_; 
v___x_611_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_516_ = v___x_611_;
goto v___jp_515_;
}
else
{
lean_object* v___x_612_; 
v___x_612_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_516_ = v___x_612_;
goto v___jp_515_;
}
}
case 14:
{
lean_object* v___x_613_; uint8_t v___x_614_; 
v___x_613_ = lean_unsigned_to_nat(1024u);
v___x_614_ = lean_nat_dec_le(v___x_613_, v_prec_423_);
if (v___x_614_ == 0)
{
lean_object* v___x_615_; 
v___x_615_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_523_ = v___x_615_;
goto v___jp_522_;
}
else
{
lean_object* v___x_616_; 
v___x_616_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_523_ = v___x_616_;
goto v___jp_522_;
}
}
case 15:
{
lean_object* v___x_617_; uint8_t v___x_618_; 
v___x_617_ = lean_unsigned_to_nat(1024u);
v___x_618_ = lean_nat_dec_le(v___x_617_, v_prec_423_);
if (v___x_618_ == 0)
{
lean_object* v___x_619_; 
v___x_619_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_530_ = v___x_619_;
goto v___jp_529_;
}
else
{
lean_object* v___x_620_; 
v___x_620_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_530_ = v___x_620_;
goto v___jp_529_;
}
}
case 16:
{
lean_object* v___x_621_; uint8_t v___x_622_; 
v___x_621_ = lean_unsigned_to_nat(1024u);
v___x_622_ = lean_nat_dec_le(v___x_621_, v_prec_423_);
if (v___x_622_ == 0)
{
lean_object* v___x_623_; 
v___x_623_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_537_ = v___x_623_;
goto v___jp_536_;
}
else
{
lean_object* v___x_624_; 
v___x_624_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_537_ = v___x_624_;
goto v___jp_536_;
}
}
case 17:
{
lean_object* v___x_625_; uint8_t v___x_626_; 
v___x_625_ = lean_unsigned_to_nat(1024u);
v___x_626_ = lean_nat_dec_le(v___x_625_, v_prec_423_);
if (v___x_626_ == 0)
{
lean_object* v___x_627_; 
v___x_627_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_544_ = v___x_627_;
goto v___jp_543_;
}
else
{
lean_object* v___x_628_; 
v___x_628_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_544_ = v___x_628_;
goto v___jp_543_;
}
}
default: 
{
lean_object* v___x_629_; uint8_t v___x_630_; 
v___x_629_ = lean_unsigned_to_nat(1024u);
v___x_630_ = lean_nat_dec_le(v___x_629_, v_prec_423_);
if (v___x_630_ == 0)
{
lean_object* v___x_631_; 
v___x_631_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__38);
v___y_551_ = v___x_631_;
goto v___jp_550_;
}
else
{
lean_object* v___x_632_; 
v___x_632_ = lean_obj_once(&lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39, &lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39_once, _init_lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__39);
v___y_551_ = v___x_632_;
goto v___jp_550_;
}
}
}
v___jp_424_:
{
lean_object* v___x_426_; lean_object* v___x_427_; uint8_t v___x_428_; lean_object* v___x_429_; lean_object* v___x_430_; 
v___x_426_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__1));
lean_inc(v___y_425_);
v___x_427_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_427_, 0, v___y_425_);
lean_ctor_set(v___x_427_, 1, v___x_426_);
v___x_428_ = 0;
v___x_429_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_429_, 0, v___x_427_);
lean_ctor_set_uint8(v___x_429_, sizeof(void*)*1, v___x_428_);
v___x_430_ = l_Repr_addAppParen(v___x_429_, v_prec_423_);
return v___x_430_;
}
v___jp_431_:
{
lean_object* v___x_433_; lean_object* v___x_434_; uint8_t v___x_435_; lean_object* v___x_436_; lean_object* v___x_437_; 
v___x_433_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__3));
lean_inc(v___y_432_);
v___x_434_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_434_, 0, v___y_432_);
lean_ctor_set(v___x_434_, 1, v___x_433_);
v___x_435_ = 0;
v___x_436_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_436_, 0, v___x_434_);
lean_ctor_set_uint8(v___x_436_, sizeof(void*)*1, v___x_435_);
v___x_437_ = l_Repr_addAppParen(v___x_436_, v_prec_423_);
return v___x_437_;
}
v___jp_438_:
{
lean_object* v___x_440_; lean_object* v___x_441_; uint8_t v___x_442_; lean_object* v___x_443_; lean_object* v___x_444_; 
v___x_440_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__5));
lean_inc(v___y_439_);
v___x_441_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_441_, 0, v___y_439_);
lean_ctor_set(v___x_441_, 1, v___x_440_);
v___x_442_ = 0;
v___x_443_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_443_, 0, v___x_441_);
lean_ctor_set_uint8(v___x_443_, sizeof(void*)*1, v___x_442_);
v___x_444_ = l_Repr_addAppParen(v___x_443_, v_prec_423_);
return v___x_444_;
}
v___jp_445_:
{
lean_object* v___x_447_; lean_object* v___x_448_; uint8_t v___x_449_; lean_object* v___x_450_; lean_object* v___x_451_; 
v___x_447_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__7));
lean_inc(v___y_446_);
v___x_448_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_448_, 0, v___y_446_);
lean_ctor_set(v___x_448_, 1, v___x_447_);
v___x_449_ = 0;
v___x_450_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_450_, 0, v___x_448_);
lean_ctor_set_uint8(v___x_450_, sizeof(void*)*1, v___x_449_);
v___x_451_ = l_Repr_addAppParen(v___x_450_, v_prec_423_);
return v___x_451_;
}
v___jp_452_:
{
lean_object* v___x_454_; lean_object* v___x_455_; uint8_t v___x_456_; lean_object* v___x_457_; lean_object* v___x_458_; 
v___x_454_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__9));
lean_inc(v___y_453_);
v___x_455_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_455_, 0, v___y_453_);
lean_ctor_set(v___x_455_, 1, v___x_454_);
v___x_456_ = 0;
v___x_457_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_457_, 0, v___x_455_);
lean_ctor_set_uint8(v___x_457_, sizeof(void*)*1, v___x_456_);
v___x_458_ = l_Repr_addAppParen(v___x_457_, v_prec_423_);
return v___x_458_;
}
v___jp_459_:
{
lean_object* v___x_461_; lean_object* v___x_462_; uint8_t v___x_463_; lean_object* v___x_464_; lean_object* v___x_465_; 
v___x_461_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__11));
lean_inc(v___y_460_);
v___x_462_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_462_, 0, v___y_460_);
lean_ctor_set(v___x_462_, 1, v___x_461_);
v___x_463_ = 0;
v___x_464_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_464_, 0, v___x_462_);
lean_ctor_set_uint8(v___x_464_, sizeof(void*)*1, v___x_463_);
v___x_465_ = l_Repr_addAppParen(v___x_464_, v_prec_423_);
return v___x_465_;
}
v___jp_466_:
{
lean_object* v___x_468_; lean_object* v___x_469_; uint8_t v___x_470_; lean_object* v___x_471_; lean_object* v___x_472_; 
v___x_468_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__13));
lean_inc(v___y_467_);
v___x_469_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_469_, 0, v___y_467_);
lean_ctor_set(v___x_469_, 1, v___x_468_);
v___x_470_ = 0;
v___x_471_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_471_, 0, v___x_469_);
lean_ctor_set_uint8(v___x_471_, sizeof(void*)*1, v___x_470_);
v___x_472_ = l_Repr_addAppParen(v___x_471_, v_prec_423_);
return v___x_472_;
}
v___jp_473_:
{
lean_object* v___x_475_; lean_object* v___x_476_; uint8_t v___x_477_; lean_object* v___x_478_; lean_object* v___x_479_; 
v___x_475_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__15));
lean_inc(v___y_474_);
v___x_476_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_476_, 0, v___y_474_);
lean_ctor_set(v___x_476_, 1, v___x_475_);
v___x_477_ = 0;
v___x_478_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_478_, 0, v___x_476_);
lean_ctor_set_uint8(v___x_478_, sizeof(void*)*1, v___x_477_);
v___x_479_ = l_Repr_addAppParen(v___x_478_, v_prec_423_);
return v___x_479_;
}
v___jp_480_:
{
lean_object* v___x_482_; lean_object* v___x_483_; uint8_t v___x_484_; lean_object* v___x_485_; lean_object* v___x_486_; 
v___x_482_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__17));
lean_inc(v___y_481_);
v___x_483_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_483_, 0, v___y_481_);
lean_ctor_set(v___x_483_, 1, v___x_482_);
v___x_484_ = 0;
v___x_485_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_485_, 0, v___x_483_);
lean_ctor_set_uint8(v___x_485_, sizeof(void*)*1, v___x_484_);
v___x_486_ = l_Repr_addAppParen(v___x_485_, v_prec_423_);
return v___x_486_;
}
v___jp_487_:
{
lean_object* v___x_489_; lean_object* v___x_490_; uint8_t v___x_491_; lean_object* v___x_492_; lean_object* v___x_493_; 
v___x_489_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__19));
lean_inc(v___y_488_);
v___x_490_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_490_, 0, v___y_488_);
lean_ctor_set(v___x_490_, 1, v___x_489_);
v___x_491_ = 0;
v___x_492_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_492_, 0, v___x_490_);
lean_ctor_set_uint8(v___x_492_, sizeof(void*)*1, v___x_491_);
v___x_493_ = l_Repr_addAppParen(v___x_492_, v_prec_423_);
return v___x_493_;
}
v___jp_494_:
{
lean_object* v___x_496_; lean_object* v___x_497_; uint8_t v___x_498_; lean_object* v___x_499_; lean_object* v___x_500_; 
v___x_496_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__21));
lean_inc(v___y_495_);
v___x_497_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_497_, 0, v___y_495_);
lean_ctor_set(v___x_497_, 1, v___x_496_);
v___x_498_ = 0;
v___x_499_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_499_, 0, v___x_497_);
lean_ctor_set_uint8(v___x_499_, sizeof(void*)*1, v___x_498_);
v___x_500_ = l_Repr_addAppParen(v___x_499_, v_prec_423_);
return v___x_500_;
}
v___jp_501_:
{
lean_object* v___x_503_; lean_object* v___x_504_; uint8_t v___x_505_; lean_object* v___x_506_; lean_object* v___x_507_; 
v___x_503_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__23));
lean_inc(v___y_502_);
v___x_504_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_504_, 0, v___y_502_);
lean_ctor_set(v___x_504_, 1, v___x_503_);
v___x_505_ = 0;
v___x_506_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_506_, 0, v___x_504_);
lean_ctor_set_uint8(v___x_506_, sizeof(void*)*1, v___x_505_);
v___x_507_ = l_Repr_addAppParen(v___x_506_, v_prec_423_);
return v___x_507_;
}
v___jp_508_:
{
lean_object* v___x_510_; lean_object* v___x_511_; uint8_t v___x_512_; lean_object* v___x_513_; lean_object* v___x_514_; 
v___x_510_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__25));
lean_inc(v___y_509_);
v___x_511_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_511_, 0, v___y_509_);
lean_ctor_set(v___x_511_, 1, v___x_510_);
v___x_512_ = 0;
v___x_513_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_513_, 0, v___x_511_);
lean_ctor_set_uint8(v___x_513_, sizeof(void*)*1, v___x_512_);
v___x_514_ = l_Repr_addAppParen(v___x_513_, v_prec_423_);
return v___x_514_;
}
v___jp_515_:
{
lean_object* v___x_517_; lean_object* v___x_518_; uint8_t v___x_519_; lean_object* v___x_520_; lean_object* v___x_521_; 
v___x_517_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__27));
lean_inc(v___y_516_);
v___x_518_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_518_, 0, v___y_516_);
lean_ctor_set(v___x_518_, 1, v___x_517_);
v___x_519_ = 0;
v___x_520_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_520_, 0, v___x_518_);
lean_ctor_set_uint8(v___x_520_, sizeof(void*)*1, v___x_519_);
v___x_521_ = l_Repr_addAppParen(v___x_520_, v_prec_423_);
return v___x_521_;
}
v___jp_522_:
{
lean_object* v___x_524_; lean_object* v___x_525_; uint8_t v___x_526_; lean_object* v___x_527_; lean_object* v___x_528_; 
v___x_524_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__29));
lean_inc(v___y_523_);
v___x_525_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_525_, 0, v___y_523_);
lean_ctor_set(v___x_525_, 1, v___x_524_);
v___x_526_ = 0;
v___x_527_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_527_, 0, v___x_525_);
lean_ctor_set_uint8(v___x_527_, sizeof(void*)*1, v___x_526_);
v___x_528_ = l_Repr_addAppParen(v___x_527_, v_prec_423_);
return v___x_528_;
}
v___jp_529_:
{
lean_object* v___x_531_; lean_object* v___x_532_; uint8_t v___x_533_; lean_object* v___x_534_; lean_object* v___x_535_; 
v___x_531_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__31));
lean_inc(v___y_530_);
v___x_532_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_532_, 0, v___y_530_);
lean_ctor_set(v___x_532_, 1, v___x_531_);
v___x_533_ = 0;
v___x_534_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_534_, 0, v___x_532_);
lean_ctor_set_uint8(v___x_534_, sizeof(void*)*1, v___x_533_);
v___x_535_ = l_Repr_addAppParen(v___x_534_, v_prec_423_);
return v___x_535_;
}
v___jp_536_:
{
lean_object* v___x_538_; lean_object* v___x_539_; uint8_t v___x_540_; lean_object* v___x_541_; lean_object* v___x_542_; 
v___x_538_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__33));
lean_inc(v___y_537_);
v___x_539_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_539_, 0, v___y_537_);
lean_ctor_set(v___x_539_, 1, v___x_538_);
v___x_540_ = 0;
v___x_541_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_541_, 0, v___x_539_);
lean_ctor_set_uint8(v___x_541_, sizeof(void*)*1, v___x_540_);
v___x_542_ = l_Repr_addAppParen(v___x_541_, v_prec_423_);
return v___x_542_;
}
v___jp_543_:
{
lean_object* v___x_545_; lean_object* v___x_546_; uint8_t v___x_547_; lean_object* v___x_548_; lean_object* v___x_549_; 
v___x_545_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__35));
lean_inc(v___y_544_);
v___x_546_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_546_, 0, v___y_544_);
lean_ctor_set(v___x_546_, 1, v___x_545_);
v___x_547_ = 0;
v___x_548_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_548_, 0, v___x_546_);
lean_ctor_set_uint8(v___x_548_, sizeof(void*)*1, v___x_547_);
v___x_549_ = l_Repr_addAppParen(v___x_548_, v_prec_423_);
return v___x_549_;
}
v___jp_550_:
{
lean_object* v___x_552_; lean_object* v___x_553_; uint8_t v___x_554_; lean_object* v___x_555_; lean_object* v___x_556_; 
v___x_552_ = ((lean_object*)(lp_WearHexagon_WearHexagon_instReprActivity_repr___closed__37));
lean_inc(v___y_551_);
v___x_553_ = lean_alloc_ctor(4, 2, 0);
lean_ctor_set(v___x_553_, 0, v___y_551_);
lean_ctor_set(v___x_553_, 1, v___x_552_);
v___x_554_ = 0;
v___x_555_ = lean_alloc_ctor(6, 1, 1);
lean_ctor_set(v___x_555_, 0, v___x_553_);
lean_ctor_set_uint8(v___x_555_, sizeof(void*)*1, v___x_554_);
v___x_556_ = l_Repr_addAppParen(v___x_555_, v_prec_423_);
return v___x_556_;
}
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_instReprActivity_repr___boxed(lean_object* v_x_633_, lean_object* v_prec_634_){
_start:
{
uint8_t v_x_1073__boxed_635_; lean_object* v_res_636_; 
v_x_1073__boxed_635_ = lean_unbox(v_x_633_);
v_res_636_ = lp_WearHexagon_WearHexagon_instReprActivity_repr(v_x_1073__boxed_635_, v_prec_634_);
lean_dec(v_prec_634_);
return v_res_636_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_encode(uint8_t v_x_639_){
_start:
{
switch(v_x_639_)
{
case 0:
{
lean_object* v___x_640_; 
v___x_640_ = lean_unsigned_to_nat(0u);
return v___x_640_;
}
case 1:
{
lean_object* v___x_641_; 
v___x_641_ = lean_unsigned_to_nat(1u);
return v___x_641_;
}
case 2:
{
lean_object* v___x_642_; 
v___x_642_ = lean_unsigned_to_nat(2u);
return v___x_642_;
}
case 3:
{
lean_object* v___x_643_; 
v___x_643_ = lean_unsigned_to_nat(3u);
return v___x_643_;
}
case 4:
{
lean_object* v___x_644_; 
v___x_644_ = lean_unsigned_to_nat(4u);
return v___x_644_;
}
case 5:
{
lean_object* v___x_645_; 
v___x_645_ = lean_unsigned_to_nat(5u);
return v___x_645_;
}
case 6:
{
lean_object* v___x_646_; 
v___x_646_ = lean_unsigned_to_nat(6u);
return v___x_646_;
}
case 7:
{
lean_object* v___x_647_; 
v___x_647_ = lean_unsigned_to_nat(7u);
return v___x_647_;
}
case 8:
{
lean_object* v___x_648_; 
v___x_648_ = lean_unsigned_to_nat(8u);
return v___x_648_;
}
case 9:
{
lean_object* v___x_649_; 
v___x_649_ = lean_unsigned_to_nat(9u);
return v___x_649_;
}
case 10:
{
lean_object* v___x_650_; 
v___x_650_ = lean_unsigned_to_nat(10u);
return v___x_650_;
}
case 11:
{
lean_object* v___x_651_; 
v___x_651_ = lean_unsigned_to_nat(11u);
return v___x_651_;
}
case 12:
{
lean_object* v___x_652_; 
v___x_652_ = lean_unsigned_to_nat(12u);
return v___x_652_;
}
case 13:
{
lean_object* v___x_653_; 
v___x_653_ = lean_unsigned_to_nat(13u);
return v___x_653_;
}
case 14:
{
lean_object* v___x_654_; 
v___x_654_ = lean_unsigned_to_nat(14u);
return v___x_654_;
}
case 15:
{
lean_object* v___x_655_; 
v___x_655_ = lean_unsigned_to_nat(15u);
return v___x_655_;
}
case 16:
{
lean_object* v___x_656_; 
v___x_656_ = lean_unsigned_to_nat(16u);
return v___x_656_;
}
case 17:
{
lean_object* v___x_657_; 
v___x_657_ = lean_unsigned_to_nat(17u);
return v___x_657_;
}
default: 
{
lean_object* v___x_658_; 
v___x_658_ = lean_unsigned_to_nat(18u);
return v___x_658_;
}
}
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_encode___boxed(lean_object* v_x_659_){
_start:
{
uint8_t v_x_194__boxed_660_; lean_object* v_res_661_; 
v_x_194__boxed_660_ = lean_unbox(v_x_659_);
v_res_661_ = lp_WearHexagon_WearHexagon_encode(v_x_194__boxed_660_);
return v_res_661_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_decode(lean_object* v_x_719_){
_start:
{
lean_object* v___x_720_; uint8_t v___x_721_; 
v___x_720_ = lean_unsigned_to_nat(0u);
v___x_721_ = lean_nat_dec_eq(v_x_719_, v___x_720_);
if (v___x_721_ == 0)
{
lean_object* v___x_722_; uint8_t v___x_723_; 
v___x_722_ = lean_unsigned_to_nat(1u);
v___x_723_ = lean_nat_dec_eq(v_x_719_, v___x_722_);
if (v___x_723_ == 0)
{
lean_object* v___x_724_; uint8_t v___x_725_; 
v___x_724_ = lean_unsigned_to_nat(2u);
v___x_725_ = lean_nat_dec_eq(v_x_719_, v___x_724_);
if (v___x_725_ == 0)
{
lean_object* v___x_726_; uint8_t v___x_727_; 
v___x_726_ = lean_unsigned_to_nat(3u);
v___x_727_ = lean_nat_dec_eq(v_x_719_, v___x_726_);
if (v___x_727_ == 0)
{
lean_object* v___x_728_; uint8_t v___x_729_; 
v___x_728_ = lean_unsigned_to_nat(4u);
v___x_729_ = lean_nat_dec_eq(v_x_719_, v___x_728_);
if (v___x_729_ == 0)
{
lean_object* v___x_730_; uint8_t v___x_731_; 
v___x_730_ = lean_unsigned_to_nat(5u);
v___x_731_ = lean_nat_dec_eq(v_x_719_, v___x_730_);
if (v___x_731_ == 0)
{
lean_object* v___x_732_; uint8_t v___x_733_; 
v___x_732_ = lean_unsigned_to_nat(6u);
v___x_733_ = lean_nat_dec_eq(v_x_719_, v___x_732_);
if (v___x_733_ == 0)
{
lean_object* v___x_734_; uint8_t v___x_735_; 
v___x_734_ = lean_unsigned_to_nat(7u);
v___x_735_ = lean_nat_dec_eq(v_x_719_, v___x_734_);
if (v___x_735_ == 0)
{
lean_object* v___x_736_; uint8_t v___x_737_; 
v___x_736_ = lean_unsigned_to_nat(8u);
v___x_737_ = lean_nat_dec_eq(v_x_719_, v___x_736_);
if (v___x_737_ == 0)
{
lean_object* v___x_738_; uint8_t v___x_739_; 
v___x_738_ = lean_unsigned_to_nat(9u);
v___x_739_ = lean_nat_dec_eq(v_x_719_, v___x_738_);
if (v___x_739_ == 0)
{
lean_object* v___x_740_; uint8_t v___x_741_; 
v___x_740_ = lean_unsigned_to_nat(10u);
v___x_741_ = lean_nat_dec_eq(v_x_719_, v___x_740_);
if (v___x_741_ == 0)
{
lean_object* v___x_742_; uint8_t v___x_743_; 
v___x_742_ = lean_unsigned_to_nat(11u);
v___x_743_ = lean_nat_dec_eq(v_x_719_, v___x_742_);
if (v___x_743_ == 0)
{
lean_object* v___x_744_; uint8_t v___x_745_; 
v___x_744_ = lean_unsigned_to_nat(12u);
v___x_745_ = lean_nat_dec_eq(v_x_719_, v___x_744_);
if (v___x_745_ == 0)
{
lean_object* v___x_746_; uint8_t v___x_747_; 
v___x_746_ = lean_unsigned_to_nat(13u);
v___x_747_ = lean_nat_dec_eq(v_x_719_, v___x_746_);
if (v___x_747_ == 0)
{
lean_object* v___x_748_; uint8_t v___x_749_; 
v___x_748_ = lean_unsigned_to_nat(14u);
v___x_749_ = lean_nat_dec_eq(v_x_719_, v___x_748_);
if (v___x_749_ == 0)
{
lean_object* v___x_750_; uint8_t v___x_751_; 
v___x_750_ = lean_unsigned_to_nat(15u);
v___x_751_ = lean_nat_dec_eq(v_x_719_, v___x_750_);
if (v___x_751_ == 0)
{
lean_object* v___x_752_; uint8_t v___x_753_; 
v___x_752_ = lean_unsigned_to_nat(16u);
v___x_753_ = lean_nat_dec_eq(v_x_719_, v___x_752_);
if (v___x_753_ == 0)
{
lean_object* v___x_754_; uint8_t v___x_755_; 
v___x_754_ = lean_unsigned_to_nat(17u);
v___x_755_ = lean_nat_dec_eq(v_x_719_, v___x_754_);
if (v___x_755_ == 0)
{
lean_object* v___x_756_; uint8_t v___x_757_; 
v___x_756_ = lean_unsigned_to_nat(18u);
v___x_757_ = lean_nat_dec_eq(v_x_719_, v___x_756_);
if (v___x_757_ == 0)
{
lean_object* v___x_758_; 
v___x_758_ = lean_box(0);
return v___x_758_;
}
else
{
lean_object* v___x_759_; 
v___x_759_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__0));
return v___x_759_;
}
}
else
{
lean_object* v___x_760_; 
v___x_760_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__1));
return v___x_760_;
}
}
else
{
lean_object* v___x_761_; 
v___x_761_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__2));
return v___x_761_;
}
}
else
{
lean_object* v___x_762_; 
v___x_762_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__3));
return v___x_762_;
}
}
else
{
lean_object* v___x_763_; 
v___x_763_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__4));
return v___x_763_;
}
}
else
{
lean_object* v___x_764_; 
v___x_764_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__5));
return v___x_764_;
}
}
else
{
lean_object* v___x_765_; 
v___x_765_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__6));
return v___x_765_;
}
}
else
{
lean_object* v___x_766_; 
v___x_766_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__7));
return v___x_766_;
}
}
else
{
lean_object* v___x_767_; 
v___x_767_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__8));
return v___x_767_;
}
}
else
{
lean_object* v___x_768_; 
v___x_768_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__9));
return v___x_768_;
}
}
else
{
lean_object* v___x_769_; 
v___x_769_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__10));
return v___x_769_;
}
}
else
{
lean_object* v___x_770_; 
v___x_770_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__11));
return v___x_770_;
}
}
else
{
lean_object* v___x_771_; 
v___x_771_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__12));
return v___x_771_;
}
}
else
{
lean_object* v___x_772_; 
v___x_772_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__13));
return v___x_772_;
}
}
else
{
lean_object* v___x_773_; 
v___x_773_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__14));
return v___x_773_;
}
}
else
{
lean_object* v___x_774_; 
v___x_774_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__15));
return v___x_774_;
}
}
else
{
lean_object* v___x_775_; 
v___x_775_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__16));
return v___x_775_;
}
}
else
{
lean_object* v___x_776_; 
v___x_776_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__17));
return v___x_776_;
}
}
else
{
lean_object* v___x_777_; 
v___x_777_ = ((lean_object*)(lp_WearHexagon_WearHexagon_decode___closed__18));
return v___x_777_;
}
}
}
LEAN_EXPORT lean_object* lp_WearHexagon_WearHexagon_decode___boxed(lean_object* v_x_778_){
_start:
{
lean_object* v_res_779_; 
v_res_779_ = lp_WearHexagon_WearHexagon_decode(v_x_778_);
lean_dec(v_x_778_);
return v_res_779_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon___private_WearHexagon_0__WearHexagon_instReprActivity_repr_match__1_splitter___redArg(uint8_t v_x_780_, lean_object* v_h__1_781_, lean_object* v_h__2_782_, lean_object* v_h__3_783_, lean_object* v_h__4_784_, lean_object* v_h__5_785_, lean_object* v_h__6_786_, lean_object* v_h__7_787_, lean_object* v_h__8_788_, lean_object* v_h__9_789_, lean_object* v_h__10_790_, lean_object* v_h__11_791_, lean_object* v_h__12_792_, lean_object* v_h__13_793_, lean_object* v_h__14_794_, lean_object* v_h__15_795_, lean_object* v_h__16_796_, lean_object* v_h__17_797_, lean_object* v_h__18_798_, lean_object* v_h__19_799_){
_start:
{
switch(v_x_780_)
{
case 0:
{
lean_object* v___x_800_; lean_object* v___x_801_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
v___x_800_ = lean_box(0);
v___x_801_ = lean_apply_1(v_h__1_781_, v___x_800_);
return v___x_801_;
}
case 1:
{
lean_object* v___x_802_; lean_object* v___x_803_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__1_781_);
v___x_802_ = lean_box(0);
v___x_803_ = lean_apply_1(v_h__2_782_, v___x_802_);
return v___x_803_;
}
case 2:
{
lean_object* v___x_804_; lean_object* v___x_805_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_804_ = lean_box(0);
v___x_805_ = lean_apply_1(v_h__3_783_, v___x_804_);
return v___x_805_;
}
case 3:
{
lean_object* v___x_806_; lean_object* v___x_807_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_806_ = lean_box(0);
v___x_807_ = lean_apply_1(v_h__4_784_, v___x_806_);
return v___x_807_;
}
case 4:
{
lean_object* v___x_808_; lean_object* v___x_809_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_808_ = lean_box(0);
v___x_809_ = lean_apply_1(v_h__5_785_, v___x_808_);
return v___x_809_;
}
case 5:
{
lean_object* v___x_810_; lean_object* v___x_811_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_810_ = lean_box(0);
v___x_811_ = lean_apply_1(v_h__6_786_, v___x_810_);
return v___x_811_;
}
case 6:
{
lean_object* v___x_812_; lean_object* v___x_813_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_812_ = lean_box(0);
v___x_813_ = lean_apply_1(v_h__7_787_, v___x_812_);
return v___x_813_;
}
case 7:
{
lean_object* v___x_814_; lean_object* v___x_815_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_814_ = lean_box(0);
v___x_815_ = lean_apply_1(v_h__8_788_, v___x_814_);
return v___x_815_;
}
case 8:
{
lean_object* v___x_816_; lean_object* v___x_817_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_816_ = lean_box(0);
v___x_817_ = lean_apply_1(v_h__9_789_, v___x_816_);
return v___x_817_;
}
case 9:
{
lean_object* v___x_818_; lean_object* v___x_819_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_818_ = lean_box(0);
v___x_819_ = lean_apply_1(v_h__10_790_, v___x_818_);
return v___x_819_;
}
case 10:
{
lean_object* v___x_820_; lean_object* v___x_821_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_820_ = lean_box(0);
v___x_821_ = lean_apply_1(v_h__11_791_, v___x_820_);
return v___x_821_;
}
case 11:
{
lean_object* v___x_822_; lean_object* v___x_823_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_822_ = lean_box(0);
v___x_823_ = lean_apply_1(v_h__12_792_, v___x_822_);
return v___x_823_;
}
case 12:
{
lean_object* v___x_824_; lean_object* v___x_825_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_824_ = lean_box(0);
v___x_825_ = lean_apply_1(v_h__13_793_, v___x_824_);
return v___x_825_;
}
case 13:
{
lean_object* v___x_826_; lean_object* v___x_827_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_826_ = lean_box(0);
v___x_827_ = lean_apply_1(v_h__14_794_, v___x_826_);
return v___x_827_;
}
case 14:
{
lean_object* v___x_828_; lean_object* v___x_829_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_828_ = lean_box(0);
v___x_829_ = lean_apply_1(v_h__15_795_, v___x_828_);
return v___x_829_;
}
case 15:
{
lean_object* v___x_830_; lean_object* v___x_831_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_830_ = lean_box(0);
v___x_831_ = lean_apply_1(v_h__16_796_, v___x_830_);
return v___x_831_;
}
case 16:
{
lean_object* v___x_832_; lean_object* v___x_833_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__18_798_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_832_ = lean_box(0);
v___x_833_ = lean_apply_1(v_h__17_797_, v___x_832_);
return v___x_833_;
}
case 17:
{
lean_object* v___x_834_; lean_object* v___x_835_; 
lean_dec(v_h__19_799_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_834_ = lean_box(0);
v___x_835_ = lean_apply_1(v_h__18_798_, v___x_834_);
return v___x_835_;
}
default: 
{
lean_object* v___x_836_; lean_object* v___x_837_; 
lean_dec(v_h__18_798_);
lean_dec(v_h__17_797_);
lean_dec(v_h__16_796_);
lean_dec(v_h__15_795_);
lean_dec(v_h__14_794_);
lean_dec(v_h__13_793_);
lean_dec(v_h__12_792_);
lean_dec(v_h__11_791_);
lean_dec(v_h__10_790_);
lean_dec(v_h__9_789_);
lean_dec(v_h__8_788_);
lean_dec(v_h__7_787_);
lean_dec(v_h__6_786_);
lean_dec(v_h__5_785_);
lean_dec(v_h__4_784_);
lean_dec(v_h__3_783_);
lean_dec(v_h__2_782_);
lean_dec(v_h__1_781_);
v___x_836_ = lean_box(0);
v___x_837_ = lean_apply_1(v_h__19_799_, v___x_836_);
return v___x_837_;
}
}
}
}
LEAN_EXPORT lean_object* lp_WearHexagon___private_WearHexagon_0__WearHexagon_instReprActivity_repr_match__1_splitter___redArg___boxed(lean_object** _args){
lean_object* v_x_838_ = _args[0];
lean_object* v_h__1_839_ = _args[1];
lean_object* v_h__2_840_ = _args[2];
lean_object* v_h__3_841_ = _args[3];
lean_object* v_h__4_842_ = _args[4];
lean_object* v_h__5_843_ = _args[5];
lean_object* v_h__6_844_ = _args[6];
lean_object* v_h__7_845_ = _args[7];
lean_object* v_h__8_846_ = _args[8];
lean_object* v_h__9_847_ = _args[9];
lean_object* v_h__10_848_ = _args[10];
lean_object* v_h__11_849_ = _args[11];
lean_object* v_h__12_850_ = _args[12];
lean_object* v_h__13_851_ = _args[13];
lean_object* v_h__14_852_ = _args[14];
lean_object* v_h__15_853_ = _args[15];
lean_object* v_h__16_854_ = _args[16];
lean_object* v_h__17_855_ = _args[17];
lean_object* v_h__18_856_ = _args[18];
lean_object* v_h__19_857_ = _args[19];
_start:
{
uint8_t v_x_196__boxed_858_; lean_object* v_res_859_; 
v_x_196__boxed_858_ = lean_unbox(v_x_838_);
v_res_859_ = lp_WearHexagon___private_WearHexagon_0__WearHexagon_instReprActivity_repr_match__1_splitter___redArg(v_x_196__boxed_858_, v_h__1_839_, v_h__2_840_, v_h__3_841_, v_h__4_842_, v_h__5_843_, v_h__6_844_, v_h__7_845_, v_h__8_846_, v_h__9_847_, v_h__10_848_, v_h__11_849_, v_h__12_850_, v_h__13_851_, v_h__14_852_, v_h__15_853_, v_h__16_854_, v_h__17_855_, v_h__18_856_, v_h__19_857_);
return v_res_859_;
}
}
LEAN_EXPORT lean_object* lp_WearHexagon___private_WearHexagon_0__WearHexagon_instReprActivity_repr_match__1_splitter(lean_object* v_motive_860_, uint8_t v_x_861_, lean_object* v_h__1_862_, lean_object* v_h__2_863_, lean_object* v_h__3_864_, lean_object* v_h__4_865_, lean_object* v_h__5_866_, lean_object* v_h__6_867_, lean_object* v_h__7_868_, lean_object* v_h__8_869_, lean_object* v_h__9_870_, lean_object* v_h__10_871_, lean_object* v_h__11_872_, lean_object* v_h__12_873_, lean_object* v_h__13_874_, lean_object* v_h__14_875_, lean_object* v_h__15_876_, lean_object* v_h__16_877_, lean_object* v_h__17_878_, lean_object* v_h__18_879_, lean_object* v_h__19_880_){
_start:
{
switch(v_x_861_)
{
case 0:
{
lean_object* v___x_881_; lean_object* v___x_882_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
v___x_881_ = lean_box(0);
v___x_882_ = lean_apply_1(v_h__1_862_, v___x_881_);
return v___x_882_;
}
case 1:
{
lean_object* v___x_883_; lean_object* v___x_884_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__1_862_);
v___x_883_ = lean_box(0);
v___x_884_ = lean_apply_1(v_h__2_863_, v___x_883_);
return v___x_884_;
}
case 2:
{
lean_object* v___x_885_; lean_object* v___x_886_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_885_ = lean_box(0);
v___x_886_ = lean_apply_1(v_h__3_864_, v___x_885_);
return v___x_886_;
}
case 3:
{
lean_object* v___x_887_; lean_object* v___x_888_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_887_ = lean_box(0);
v___x_888_ = lean_apply_1(v_h__4_865_, v___x_887_);
return v___x_888_;
}
case 4:
{
lean_object* v___x_889_; lean_object* v___x_890_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_889_ = lean_box(0);
v___x_890_ = lean_apply_1(v_h__5_866_, v___x_889_);
return v___x_890_;
}
case 5:
{
lean_object* v___x_891_; lean_object* v___x_892_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_891_ = lean_box(0);
v___x_892_ = lean_apply_1(v_h__6_867_, v___x_891_);
return v___x_892_;
}
case 6:
{
lean_object* v___x_893_; lean_object* v___x_894_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_893_ = lean_box(0);
v___x_894_ = lean_apply_1(v_h__7_868_, v___x_893_);
return v___x_894_;
}
case 7:
{
lean_object* v___x_895_; lean_object* v___x_896_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_895_ = lean_box(0);
v___x_896_ = lean_apply_1(v_h__8_869_, v___x_895_);
return v___x_896_;
}
case 8:
{
lean_object* v___x_897_; lean_object* v___x_898_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_897_ = lean_box(0);
v___x_898_ = lean_apply_1(v_h__9_870_, v___x_897_);
return v___x_898_;
}
case 9:
{
lean_object* v___x_899_; lean_object* v___x_900_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_899_ = lean_box(0);
v___x_900_ = lean_apply_1(v_h__10_871_, v___x_899_);
return v___x_900_;
}
case 10:
{
lean_object* v___x_901_; lean_object* v___x_902_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_901_ = lean_box(0);
v___x_902_ = lean_apply_1(v_h__11_872_, v___x_901_);
return v___x_902_;
}
case 11:
{
lean_object* v___x_903_; lean_object* v___x_904_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_903_ = lean_box(0);
v___x_904_ = lean_apply_1(v_h__12_873_, v___x_903_);
return v___x_904_;
}
case 12:
{
lean_object* v___x_905_; lean_object* v___x_906_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_905_ = lean_box(0);
v___x_906_ = lean_apply_1(v_h__13_874_, v___x_905_);
return v___x_906_;
}
case 13:
{
lean_object* v___x_907_; lean_object* v___x_908_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_907_ = lean_box(0);
v___x_908_ = lean_apply_1(v_h__14_875_, v___x_907_);
return v___x_908_;
}
case 14:
{
lean_object* v___x_909_; lean_object* v___x_910_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_909_ = lean_box(0);
v___x_910_ = lean_apply_1(v_h__15_876_, v___x_909_);
return v___x_910_;
}
case 15:
{
lean_object* v___x_911_; lean_object* v___x_912_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_911_ = lean_box(0);
v___x_912_ = lean_apply_1(v_h__16_877_, v___x_911_);
return v___x_912_;
}
case 16:
{
lean_object* v___x_913_; lean_object* v___x_914_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__18_879_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_913_ = lean_box(0);
v___x_914_ = lean_apply_1(v_h__17_878_, v___x_913_);
return v___x_914_;
}
case 17:
{
lean_object* v___x_915_; lean_object* v___x_916_; 
lean_dec(v_h__19_880_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_915_ = lean_box(0);
v___x_916_ = lean_apply_1(v_h__18_879_, v___x_915_);
return v___x_916_;
}
default: 
{
lean_object* v___x_917_; lean_object* v___x_918_; 
lean_dec(v_h__18_879_);
lean_dec(v_h__17_878_);
lean_dec(v_h__16_877_);
lean_dec(v_h__15_876_);
lean_dec(v_h__14_875_);
lean_dec(v_h__13_874_);
lean_dec(v_h__12_873_);
lean_dec(v_h__11_872_);
lean_dec(v_h__10_871_);
lean_dec(v_h__9_870_);
lean_dec(v_h__8_869_);
lean_dec(v_h__7_868_);
lean_dec(v_h__6_867_);
lean_dec(v_h__5_866_);
lean_dec(v_h__4_865_);
lean_dec(v_h__3_864_);
lean_dec(v_h__2_863_);
lean_dec(v_h__1_862_);
v___x_917_ = lean_box(0);
v___x_918_ = lean_apply_1(v_h__19_880_, v___x_917_);
return v___x_918_;
}
}
}
}
LEAN_EXPORT lean_object* lp_WearHexagon___private_WearHexagon_0__WearHexagon_instReprActivity_repr_match__1_splitter___boxed(lean_object** _args){
lean_object* v_motive_919_ = _args[0];
lean_object* v_x_920_ = _args[1];
lean_object* v_h__1_921_ = _args[2];
lean_object* v_h__2_922_ = _args[3];
lean_object* v_h__3_923_ = _args[4];
lean_object* v_h__4_924_ = _args[5];
lean_object* v_h__5_925_ = _args[6];
lean_object* v_h__6_926_ = _args[7];
lean_object* v_h__7_927_ = _args[8];
lean_object* v_h__8_928_ = _args[9];
lean_object* v_h__9_929_ = _args[10];
lean_object* v_h__10_930_ = _args[11];
lean_object* v_h__11_931_ = _args[12];
lean_object* v_h__12_932_ = _args[13];
lean_object* v_h__13_933_ = _args[14];
lean_object* v_h__14_934_ = _args[15];
lean_object* v_h__15_935_ = _args[16];
lean_object* v_h__16_936_ = _args[17];
lean_object* v_h__17_937_ = _args[18];
lean_object* v_h__18_938_ = _args[19];
lean_object* v_h__19_939_ = _args[20];
_start:
{
uint8_t v_x_275__boxed_940_; lean_object* v_res_941_; 
v_x_275__boxed_940_ = lean_unbox(v_x_920_);
v_res_941_ = lp_WearHexagon___private_WearHexagon_0__WearHexagon_instReprActivity_repr_match__1_splitter(v_motive_919_, v_x_275__boxed_940_, v_h__1_921_, v_h__2_922_, v_h__3_923_, v_h__4_924_, v_h__5_925_, v_h__6_926_, v_h__7_927_, v_h__8_928_, v_h__9_929_, v_h__10_930_, v_h__11_931_, v_h__12_932_, v_h__13_933_, v_h__14_934_, v_h__15_935_, v_h__16_936_, v_h__17_937_, v_h__18_938_, v_h__19_939_);
return v_res_941_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_plausible_Plausible(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_WearHexagon_WearHexagon(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_plausible_Plausible(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
