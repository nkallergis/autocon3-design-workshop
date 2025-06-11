"""Basic design demonstrates the capabilities of the Design Builder."""
from nautobot.apps.jobs import register_jobs, StringVar, ObjectVar, BooleanVar

from nautobot.dcim.models import Location

from nautobot_design_builder.choices import DesignModeChoices
from nautobot_design_builder.contrib import ext
from nautobot_design_builder.design_job import DesignJob

from .context import BranchDesignContext

name = "Branch Site Jobs"

class BranchDesign(DesignJob):
    """A basic design for design builder."""

    region = ObjectVar(
        label="Region",
        description="Region for the new branch",
        model=Location,
    )
    site_name = StringVar(label="Site Name", regex=r"\w{3}\d+")
    lab_topology = BooleanVar(label="Containerlab topology?", default=False, description="Generate a digital twin for the design (containerlab).")

    class Meta:
        """Metadata describing this design job."""

        design_mode = DesignModeChoices.DEPLOYMENT
        name = "Deploy Branch Site with Design Builder"
        description = "Create a new branch site."
        version = "1.0"
        docs = "A basic design for new branches."
        nautobot_version = ">=2"
        has_sensitive_variables = False
        extensions = [ext.CableConnectionExtension, ext.NextPrefixExtension]
        design_file = "designs/0001_branchdesign.yaml.j2"
        context_class = BranchDesignContext

register_jobs(BranchDesign)
