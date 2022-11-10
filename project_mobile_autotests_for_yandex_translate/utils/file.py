def abs_path_from_project(relative_path: str):
    import project_mobile_autotests_for_yandex_translate
    from pathlib import Path

    return (
        Path(project_mobile_autotests_for_yandex_translate.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
