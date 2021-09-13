from GuideToExile.data_classes import PobDetails
from GuideToExile.models import BuildGuide, UniqueItem, Keystone, AscendancyClass, ActiveSkill, UserProfile
from GuideToExile.skill_tree import SkillTreeService


def create_build_guide(author: UserProfile, build_details: PobDetails, pob_string: str,
                       skill_tree_service: SkillTreeService, text: str = 'Content',
                       title: str = 'Title') -> BuildGuide:
    keystones = get_or_create_keystones(build_details, skill_tree_service)
    unique_items = get_or_create_unique_items(build_details)
    asc_class = get_asc_class(build_details)

    new_guide = BuildGuide(title=title,
                           pob_details=build_details,
                           pob_string=pob_string,
                           text=text,
                           ascendancy_class=asc_class,
                           )
    new_guide.save()

    primary_active_skill = ActiveSkill.objects.get(name=build_details.imported_primary_skill)
    new_guide.primary_skills.add(primary_active_skill)
    new_guide.author = author
    new_guide.keystones.set(keystones)
    new_guide.unique_items.set(unique_items)

    return new_guide


def get_asc_class(pob_details: PobDetails) -> AscendancyClass:
    asc_name = pob_details.ascendancy_name
    asc_name_id = AscendancyClass.AscClassName[asc_name.upper()]
    base_class_name = pob_details.class_name
    base_class_name_id = AscendancyClass.BaseClassName[base_class_name.upper()]
    asc_class = AscendancyClass.objects.get(name=asc_name_id, base_class_name=base_class_name_id)

    return asc_class


def get_or_create_unique_items(pob_details: PobDetails) -> list[UniqueItem]:
    unique_items_names = [item.name for item in pob_details.items if item.rarity == 'UNIQUE']
    unique_items = [UniqueItem.objects.get_or_create(name=name)[0] for name in unique_items_names]
    for item in unique_items:
        item.save()
    return unique_items


def get_or_create_keystones(pob_details: PobDetails, skill_tree_service: SkillTreeService) -> list[Keystone]:
    keystone_names = []
    for tree_spec in pob_details.tree_specs:
        all_nodes = skill_tree_service.skill_trees[tree_spec.tree_version].nodes
        keystone_names.extend(all_nodes[node_id].name for node_id in tree_spec.nodes if
                              node_id in all_nodes and all_nodes[node_id].is_keystone)

    keystones = [Keystone.objects.get_or_create(name=name)[0] for name in set(keystone_names)]
    for keystone in keystones:
        keystone.save()
    return keystones
